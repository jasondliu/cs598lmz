import socket
socket.if_indextoname(3) # returns ['wlp2s0']

def get_ips():
    for interface in netifaces.interfaces():
        if interface not in ['lo', 'docker0']:
            yield netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']

for ip in get_ips():
    print(ip)
