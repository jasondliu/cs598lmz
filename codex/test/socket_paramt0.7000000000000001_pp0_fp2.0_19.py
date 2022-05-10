import socket
socket.if_indextoname(0)

import subprocess
proc = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
output = proc.stdout.read()
print (output)

import netifaces
netifaces.interfaces()

import netifaces
