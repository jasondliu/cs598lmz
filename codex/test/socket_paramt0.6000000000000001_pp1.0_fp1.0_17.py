import socket
socket.if_indextoname(2)

#ifconfig
import os
os.system("ifconfig")

#ifconfig -a
import os
os.system("ifconfig -a")

#ifconfig -a | grep HWaddr
import os
os.system("ifconfig -a | grep HWaddr")

#ifconfig eth0
import os
os.system("ifconfig eth0")

#ifconfig eth0 192.168.1.1
import os
os.system("ifconfig eth0 192.168.1.1")

#ifconfig eth0 down
import os
os.system("ifconfig eth0 down")

#ifconfig eth0 up
import os
os.system("ifconfig eth0 up")

#ifconfig eth0 txqueuelen 1000
import os
os.system("ifconfig eth0 txqueuelen 1000")

#ifconfig eth0:0 192.168.1.2
import os
os.system("ifconfig eth0:0 192.168.1.2")

#ifconfig eth0:0 down
import os
