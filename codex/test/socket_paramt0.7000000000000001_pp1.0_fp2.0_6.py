import socket
socket.if_indextoname(socket.if_nametoindex('eth0'))

#import netifaces
#netifaces.interfaces()
#netifaces.ifaddresses('eth0')
#netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']



#import subprocess
#subprocess.check_output('ifconfig eth0 | grep "inet\ " | cut -d\' \' -f10', stderr=subprocess.STDOUT, shell=True).decode('utf-8').strip()
