import socket
# Test socket.if_indextoname()
def if_indextoname(ifindex):
    try:
        return socket.if_indextoname(ifindex)
    except:
        return None

# Test socket.if_nametoindex()
def if_nametoindex(ifname):
    try:
        return socket.if_nametoindex(ifname)
    except:
        return None

# Test socket.gethostbyname()
def gethostbyname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except:
        return None

# Test socket.gethostbyname_ex()
def gethostbyname_ex(hostname):
    try:
        return socket.gethostbyname_ex(hostname)
    except:
        return None

# Test socket.gethostbyaddr()
def gethostbyaddr(ip_address):
    try:
        return socket.gethostbyaddr(ip_address)
    except:
        return None

# Test socket.getfqdn()
def getfqdn(name=
