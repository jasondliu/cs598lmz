import socket
socket.if_indextoname('5')

import netifaces as ni
print('\n'.join(['\n'.join([f'{nic} : {ip}' for ip in ni.ifaddresses(nic)[ni.AF_INET][0]['addr'].split('.')]) for nic in ni.interfaces()]))
