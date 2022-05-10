import socket
socket.if_indextoname('3')

#Add route to routing table
import subprocess
subprocess.call(["route", "add", "192.168.1.0", "192.168.1.1"])

#List all the routes
import subprocess
print subprocess.check_output(["route", "-n"])

#List all the interfaces
import netifaces
netifaces.interfaces()

#Get the MAC for an interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

#Get the IP for an interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

#Get the IP for an interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET6][0]['addr']

#Get the MAC for an interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['
