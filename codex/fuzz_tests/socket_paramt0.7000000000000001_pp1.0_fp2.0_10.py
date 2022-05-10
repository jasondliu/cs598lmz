import socket
socket.if_indextoname("1")

"/sys/class/net/eth0/address"

cmd("cat /sys/class/net/eth0/address")

#with open("/sys/class/net/eth0/address", 'r') as f:
#    print f.read()

f = open("/sys/class/net/eth0/address", 'r')
print f.read()

_ = [os.system("%s"%cmd) for cmd in cmds]

import subprocess
p = subprocess.Popen("ls", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print "output", output
