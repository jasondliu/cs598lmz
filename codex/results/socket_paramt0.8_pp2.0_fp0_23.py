import socket
socket.if_indextoname(1)

# another way of getting the IP address
# https://www.pythoncentral.io/find-public-ip-address-python-3-3/

def get_ip():
    ip_address = '';
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip_address = s.getsockname()[0]
    except:
        ip_address = '127.0.0.1'
    finally:
        s.close()
    return ip_address
print(get_ip())

# hosts file
# https://en.wikipedia.org/wiki/Hosts_(file)
# You can access the hosts file by opening /etc/hosts using a text editor. 
# \etc\hosts is part of the "bind" DNS package and it is not needed.
# http://www.howtogeek.com/howto/27350/beginner-geek-
