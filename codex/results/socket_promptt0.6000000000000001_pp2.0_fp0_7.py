import socket
# Test socket.if_indextoname()
import array

def bytes2int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def get_mac_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    mac = (':'.join(re.findall('..', '%012x' % getnode())))
    return mac

def get_host_name():
    return socket.gethostname()

def get_interface_info():
    interface_list = socket.if_nameindex()
    interface_info = {}
    for interface in interface_list:
        interface_name = socket.if_indextoname(interface
