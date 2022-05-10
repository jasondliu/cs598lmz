import socket
socket.if_indextoname(3)

def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])


print (get_mac_address())
#result = subprocess.check_output(["ifconfig", "eth0"])
#print result
#print(result.split("\n"))
#print(result.split("\n")[1].split(" "))
#print(result.split("\n")[1].split(" ")[4])

#import sys

#import subprocess

#def get_mac_address():
#    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
#    return ":".join([mac[e:e+2] for e in range(0,11,2)])

#def get_nic_ip(nic_name):
#    return subprocess.check_output(["ifconfig", nic_name]).split
