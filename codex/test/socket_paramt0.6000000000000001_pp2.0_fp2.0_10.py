import socket
socket.if_indextoname('3')

#Add route to routing table
import subprocess
subprocess.call(["route", "add", "192.168.1.0", "192.168.1.1"])

#List all the routes
import subprocess
