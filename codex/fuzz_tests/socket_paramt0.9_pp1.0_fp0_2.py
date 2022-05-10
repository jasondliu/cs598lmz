import socket
socket.if_indextoname('5')

import netifaces as ni
print('\n'.join(['\n'.join([f'{nic} : {ip}' for ip in ni.ifaddresses(nic)[ni.AF_INET][0]['addr'].split('.')]) for nic in ni.interfaces()]))
</code>
Output (IP addresses are slightly changed):
<code>lo: 127.0.0.1
lo: 0.0.0.0
lo: 255.0.0.0
lo: 127.0.0.1
enps1: 192.168.0.10
enps1: 168.0.0.0
enps1: 255.255.0.0
enps1: 192.168.0.255
enps0: 192.168.0.120
enps0: 168.0.0.0
enps0: 255.255.0.0
enps0: 192.168.0.255
enps0: 10.240.0.80
enps0: 10.240.0.0
enps0: 255
