import socket

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True


def get_ip_address(address):
    if not is_valid_ipv4_address(address):
        if not is_valid_ipv6_address(address):
            print('{0}: invalid ip address'.format(address))
            return get_host_ip(address)

    return address


def get_host_ip(address):
    return
