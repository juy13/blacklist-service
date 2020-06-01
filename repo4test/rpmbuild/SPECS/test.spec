Name:          test
Version:       1.0
Release:       1%{?dist}
Summary:       Программа студента ... группы ...
Group:         Testing
License:       GPL
URL:           https://github.com/juy13/blacklist-service
Source0:       %{name}-%{version}.tar.gz
BuildRequires: /bin/rm, /bin/mkdir, /bin/cp
Requires:      /bin/bash, /usr/bin/date
BuildArch:     noarch

%description
A test package

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 test-1.0 %{buildroot}%{_bindir}

%files
%{_bindir}/test-1.0

%changelog
* Thu Oct 16 2012 <test>
- Added %{_bindir}/test-1.0
