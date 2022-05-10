import socket
socket.if_indextoname(1)

def _ip_address(ip):
    if isinstance(ip, six.string_types):
        return ip
    else:
        return socket.inet_ntoa(addr)

def _ip_network(ip_addr, netmask):
    return '%s/%s' % (_ip_address(ip_addr), netmask)

def _normalize_ip_addr(port):
    if isinstance(port, dict):
        return port
    else:
        return {'ip_addr': port}

def get_ip_addr(ip_addr):
    if isinstance(ip_addr, dict):
        return ip_addr['ip_addr']
    else:
        return ip_addr

def get_network(port):
    if isinstance(port, dict):
        return port.get('network')
    else:
        return port

def get_port_attrs(port):
    if isinstance(port, dict):
        return port
    else:
        return {'id': port}


def get_port_id
