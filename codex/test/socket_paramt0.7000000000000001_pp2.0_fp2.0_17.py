import socket
socket.if_indextoname(socket.if_nametoindex('eth0'))

# Check to see if the interfaces are up

import os
os.system("sudo ifconfig | grep -o eth0 | grep -o eth0")
os.system("sudo ifconfig | grep -o eth1 | grep -o eth1")
os.system("sudo ifconfig | grep -o eth2 | grep -o eth2")
os.system("sudo ifconfig | grep -o eth3 | grep -o eth3")
os.system("sudo ifconfig | grep -o eth4 | grep -o eth4")
os.system("sudo ifconfig | grep -o eth5 | grep -o eth5")
os.system("sudo ifconfig | grep -o eth6 | grep -o eth6")
os.system("sudo ifconfig | grep -o eth7 | grep -o eth7")
