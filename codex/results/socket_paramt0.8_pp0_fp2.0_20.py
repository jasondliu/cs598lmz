import socket
socket.if_indextoname(3)

# Windows

import netifaces
netifaces.interfaces()

netifaces.ifaddresses('Wi-Fi')

type(netifaces.ifaddresses('Wi-Fi'))

wi_fi = netifaces.ifaddresses('Wi-Fi')[netifaces.AF_INET][0]
wi_fi

wi_fi['addr']

wi_fi['netmask']


import psutil

psutil.net_if_addrs()

psutil.net_if_stats()

interface_stats = psutil.net_if_stats()
interface_stats['Wi-Fi']

interface_stats['Wi-Fi'].isup

interface_stats['Wi-Fi'].speed

interface_stats['Wi-Fi'].duplex
