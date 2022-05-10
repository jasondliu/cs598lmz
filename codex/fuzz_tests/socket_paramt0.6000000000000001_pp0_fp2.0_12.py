import socket
socket.if_indextoname(10)

#%%

import os
import psutil
import socket

def get_ip(iface='WLAN'):
    '''
    iface: interface name as string
    '''
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.connect(('10.255.255.255', 1))
    ip = soc.getsockname()[0]
    soc.close()
    return ip

#%%

import os
import psutil
import socket

def get_ip(iface='WLAN'):
    '''
    iface: interface name as string
    '''
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.connect(('10.255.255.255', 1))
    ip = soc.getsockname()[0]
    soc.close()
    return ip

def get_interface_info(iface='WLAN'):
    '''
    iface: interface name as string
    '''
