semodule -r blacklist_serv 
./blacklist_serv.sh && semodule -i blacklist_serv.pp && semodule -e blacklist_serv && cp blacklist_serv.pp ~/rpmbuild/SOURCES/blacklist_serv-1.1 && cp blacklist_serv.te ~/rpmbuild/SOURCES/blacklist_serv-1.1 && cp blacklist_serv.fc ~/rpmbuild/SOURCES/blacklist_serv-1.1 && cp blacklist_serv.if ~/rpmbuild/SOURCES/blacklist_serv-1.1 
