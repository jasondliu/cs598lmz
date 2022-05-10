import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))
# Test socket.if_indextoname()
print(socket.if_nametoindex('lo'))
###############################
import sys
# Test sys.getwindowsversion()
v = sys.getwindowsversion()
print(v)
# Test socket.if_nametoindex()
print(v.service_pack)
###############################

#Test the option read_timeout error
import sys
import socket
import time
s = socket.socket()
timeout = 3
print("Set socket timeout is %d s." % timeout)
socket.setdefaulttimeout(timeout)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.10.250"
print("Connect to host %s." % host)
s.connect((host, 22))
#s.settimeout(timeout)
print("Training...")
time.sleep(3)
print("Sending hello...")
s.send("hello" + '\n')
