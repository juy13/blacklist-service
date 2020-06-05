#!/bin/bash

cd /rpmbuild/SOURCES && tar -cvzf blacklist_serv-1.1.tar.gz blacklist_serv-1.1 && cd ../SPECS && rpmbuild -ba blacklist_serv.spec
