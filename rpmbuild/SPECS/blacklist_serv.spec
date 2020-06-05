%define relabel_files() \
restorecon -R -v /usr/bin; \
restorecon -R -v /usr/lib/systemd/system; \

%global selinux_policyver 3.13.1-266

Name:          blacklist_serv
Version:       1.1
Release:       1%{?dist}
Summary:       A service that controls an access to specific files
Group:         B17-565 juy13
License:       MIT
URL:           https://github.com/juy13/blacklist-service
Source0:       %{name}-%{version}.tar.gz
Requires:      /bin/bash, /bin/rm, /bin/mkdir, /bin/cp, policycoreutils, policycoreutils-devel, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils, policycoreutils-devel, /usr/sbin/semodule
Requires(postun): policycoreutils, policycoreutils-devel, /usr/sbin/semodule
BuildArch:     noarch

%description
A service that can control blacklist services.
Made by Julian Voliaskiy (juy13), Salim Nurmatov, Vlad Matveev, Kalinkin Artem, Truong Thi An Hai 


%prep
%setup -q
mkdir selinux_policy
cd ../../SOURCES/%{name}-%{version}/
cp -p %{name}.if %{name}.te %{name}.fc %{name}.pp ../../BUILD/%{name}-%{version}/selinux_policy/


#%build

#cd selinux_policy/
#make -f /usr/share/selinux/devel/Makefile %{name}.pp
#cd ..

%install

cd selinux_policy/
install -d %{buildroot}%{_datadir}/selinux/
install -p -m 644 %{name}.pp %{buildroot}%{_datadir}/selinux/%{name}.pp
cd ..

mkdir -p %{buildroot}/etc/systemd/system/
mkdir -p %{buildroot}%{_bindir}/

install -m 0755 blacklist_serv.sh %{buildroot}%{_bindir}/
install -m 644 blacklist_serv.conf %{buildroot}%{_sysconfdir}/
install -m 644 blacklist_serv.service %{buildroot}%{_sysconfdir}/systemd/system/

%post
semodule -n -i %{_datadir}/selinux/%{name}.pp
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    %relabel_files
fi;

chcon -t blacklist_serv_exec_t /usr/bin/blacklist_serv.sh


%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/semodule -n -r %{modulenames} &> /dev/null || :
	if %{_sbindir}/selinuxenabled ; then
		%{_sbindir}/load_policy
		%relabel_files
	fi
fi

%files
%attr(0600,root,root) %{_datadir}/selinux/blacklist_serv.pp
%{_bindir}/blacklist_serv.sh
/etc/blacklist_serv.conf
/etc/systemd/system/blacklist_serv.service

%changelog
* Wed May 03 2020 <juy13>
- Added module SELinux











