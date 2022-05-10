import socket
socket.if_indextoname('9')

import netifaces as ni
ni.ifaddresses('wlan0')

host_ip = socket.gethostbyname(socket.gethostname())
print(host_ip)

ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr'] # use only if there is a single ip address
print(ip)

import subprocess

def get_ip(iface):
    try:
        import netifaces as ni
        return ni.ifaddresses(iface)[ni.AF_INET][0]['addr']
    except:
        pass
    try:
        import socket
        return socket.gethostbyname(socket.gethostname())
    except:
        pass
    try:
        return subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
    except:
        pass
    return None

get_ip('enp4s0')  # put your iface here
get_ip('enp4s0')
</code>
