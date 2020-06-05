#!/bin/bash

AdmFile=/etc/blacklist/blacklist.conf

function usrSignal {
 	echo "SIGUSR1"
	exit 0
}

stop_it() {
	echo "Service blacklist_serv finished."
	logger "Service blacklist_serv finished."
	sudo tail -1 /var/log/messages >> ~/blacklist.log
	exit 0
}

function test_Adm {
	local flag= $(test -f $AdmFile)
	if ($flag); then 
		logger "File exist"
		return 0
	else
		logger "No administration file"
		return 1
	fi
}

try_tofind_smth() {
	local res="$(systemctl is-active $1)"
	logger "$res"
	if [ $res = "active" ]; then
		(sudo systemctl stop $1)
		logger "$2 will be punished"
	fi		
}

function find_and_punish {
	test_Adm	
	local flag_test=$?
	#echo "Flag = $flag_test"
	if [ "$flag_test" -eq 0 ]; then
		local im="$(whoami)"
		echo "$im"
		while read SERVICE
		do
			echo "$SERVICE"
			echo "take it!"
			try_tofind_smth $SERVICE $im
		done < $AdmFile
	else
		echo "Stop"
	fi
}

trap usrSignal SIGUSR1
trap stop_it SIGINT

while true
do
	#echo "FIND"
	find_and_punish
	sleep 30 & wait
done

