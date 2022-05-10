import socket
socket.if_indextoname(4)

# get network interface ip address
from netifaces import interfaces, ifaddresses, AF_INET
def local_ip_address(ifname):
    return ifaddresses(ifname)[AF_INET][0]['addr']

local_ip_address('en0') # try 'en1' if not working on Mac OS

from netifaces import interfaces, ifaddresses
for ifname in interfaces():
    try:
        print("{} {}".format(ifname, ifaddresses(ifname)[AF_INET][0]['addr']))
    except KeyError:
        pass


# check whether ip is valid
from socket import inet_aton
def valid_ip(address):
    try:
        inet_aton(address)
        return True
    except socket.error:
        return False

valid_ip("8.8.8.8")


# get host ip
from requests import get
def get_ip_address(url):
    return get(url, headers={'User-Agent': 'Mozilla/5.0'}).
