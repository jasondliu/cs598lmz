import socket
# Test socket.if_indextoname(), socket.if_nametoindex(),
# socket.inet_addrton(), socket.inet_ntoa(),
# socket.inet_cidr_ntoa(), socket.inet_ntop() and socket.inet_pton()
my_ipv4 = socket.gethostbyname(socket.gethostname())
my_ipv6 = '2001:db8:feed:face:cafe:babe:0000:0000'
my_ipv6_prefix = '2001:db8:feed:face:cafe:babe:0000:0000/64'
prefix_len_ipv6 = 0
prefix_len_ipv4 = 0

def ipv6_prefix_len(a):
    try:
        a = int(a)
        if (a < 0 or a > 128): raise ValueError
    except: raise SystemExit('Prefix must be an int between 0 and 128')
    return a

