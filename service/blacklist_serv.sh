#!/bin/bash

AdmFile=/etc/blacklist/blacklist.conf

function usrSignal {
    echo "SIGUSR1"
}

stop_it() {
	echo "Service swap finished."
	logger "Service swap finished."
	sudo tail -1 /var/log/messages >> ~/blacklist.log
	exit 0
}

function test_Adm {
	local flag= $(test -f $AdmFile)
	if ($flag); then 
		echo "File exist"
		return 0
	else
		echo "No administration file"
		return 1
	fi
}

try_tofind_smth() {
	local res="$(systemctl is-active $1)"
	echo "$res"
	if [ $res = "active" ]; then
		(systemctl kill $1)
		echo "dude, you will be punished"
	fi		
}

function find_and_punish {
	test_Adm	
	local flag_test=$?
	#echo "Flag = $flag_test"
	if [ "$flag_test" -eq 0 ]; then
		echo "Continue"
		local im="$(whoami)"
		#echo "$im"
		while read SERVICE USER
		do
			echo "$SERVICE $USER"
			if [ $USER = $im ]; then
				echo "take it!"
				try_tofind_smth $SERVICE
			fi
		done < $AdmFile
	else
		echo "Stop"
	fi
}

trap usrSignal USR1
trap stop_it SIGINT
find_and_punish



