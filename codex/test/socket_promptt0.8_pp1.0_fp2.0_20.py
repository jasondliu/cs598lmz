import socket
# Test socket.if_indextoname
if_indextoname = sock.if_indextoname
if_indextoname.restype = c_char_p
if_indextoname.argtypes = [c_uint]

assert(if_indextoname(1) == 'eth0')

# Test socket.if_nametoindex
if_nametoindex = sock.if_nametoindex
if_nametoindex.restype = c_uint
if_nametoindex.argtypes = [c_char_p]

assert(if_nametoindex('eth0') == 1)

# Test socket.pf_packet
pf = socket.PF_PACKET
assert(socket.socket(pf, socket.SOCK_RAW, 0) != None)

# Test socket.protocol_aton/ntoa
prot_aton = sock.protocol_aton
prot_aton.restype = c_ushort
prot_aton.argtypes = [c_char_p]

prot_ntoa = sock.protocol_ntoa
