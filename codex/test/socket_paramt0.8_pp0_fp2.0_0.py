import socket
socket.if_indextoname(3)

# Interface name, IP address and MAC address
print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))
import netifaces as ni
ni.ifaddresses('en0')
ni.ifaddresses('en0')[ni.AF_LINK]

# When we only have the MAC address we can do the following
mac_to_ip = {}
for device in ni.interfaces():
    try:
        ip = ni.ifaddresses(device)[ni.AF_INET][0]['addr']
        mac_to_ip[ni.ifaddresses(device)[ni.AF_LINK][0]['addr']] = (device, ip)
    except:
        pass
ip = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']

# When we only have the IP address we can do the following
ip_to_mac = {}
