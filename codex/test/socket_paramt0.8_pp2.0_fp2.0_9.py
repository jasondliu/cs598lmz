import socket
socket.if_indextoname(12)

# my_if = netifaces.interfaces()[0]
# my_if = 'Wi-Fi'
# my_ip, my_mask = netifaces.ifaddresses(my_if)[netifaces.AF_INET][0]['addr'], \
#                  netifaces.ifaddresses(my_if)[netifaces.AF_INET][0]['netmask']
# my_mask = ipaddress.IPv4Network(my_ip + '/' + my_mask).netmask
# my_gw = netifaces.gateways()['default'][netifaces.AF_INET][0]
# my_mac = netifaces.ifaddresses(my_if)[netifaces.AF_LINK][0]['addr']

my_if = netifaces.interfaces()[5]
my_if = 'Wi-Fi'
