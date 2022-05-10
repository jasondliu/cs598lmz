import socket
import binascii

from cloudify import ctx
from cloudify.exceptions import NonRecoverableError
from cloudify.decorators import operation

from find_port import find_port

def get_manager_ip(ctx):
    try:
        return socket.gethostbyname(ctx.instance.host_ip)
    except:
        return ctx.instance.host_ip

def get_local_ip(ctx):
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return ctx.instance.host_ip

def mac_to_ip(mac):
    mac = mac.replace('-','').replace(':','')
    mac = binascii.unhexlify(mac)
    mac = [ord(x) for x in mac]
    
    mac[2] += 3
    if mac[2] > 255:
        mac[1] += 1
        mac[2] -= 256
    mac = [hex(x)[2:] for x in mac]
    mac
