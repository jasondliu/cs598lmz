import socket
socket.if_indextoname(str(2))

ifconfig -a | awk '/(cast)/ { print $2}'
 
import sys 
from subprocess import check_output as sh

def get_ifdetails():
    if len (sys.argv) == 1:
        ifname = raw_input("Choose interface to scan w/o options for list :")
        if not ifname in sh("ifconfig -a|awk '/(cast)/ { print $1}' ").split():
            print("I could not find that interface making one up for you")
            ifname = "lo"
    elif len(sys.argv) == 2:
        ifname = sys.argv[1]
        ip =  sh("ip addr show " + ifname + "|grep 'inet '|awk '{print $2}'|cut -d/ -f1")
        mac = sh("ifconfig " + ifname + "|grep 'ether '|awk '{print $2}'")
        print("for interface " + ifname)
        print("IP address : " + ip.rstrip())
