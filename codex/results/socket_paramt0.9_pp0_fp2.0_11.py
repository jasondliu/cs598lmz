import socket
socket.if_indextoname(int(if_index))
#'wlx001122334455'
socket.if_nameindex()
#[(1, 'lo'), (2, 'enp2s0'), (3, 'wlx001122334455')]
socket.if_nametoindex('enp2s0')
# 2

### inet_ntop() and inet_pton()
# These two functions perform the opposite of one another.
#    inet_pton() takes an IPv4 or IPv6 address, and turns it into python’s fixed-size format, which is a 16-byte string.
#    inet_ntop() takes the fixed-size python format, and turns it back into a human readable version.
# Here’s some examples:

# inet_pton:
socket.inet_pton(socket.AF_INET6, "2001:470:abcd:12::2")
#'\x20\x01G\x04p\xab\xcd\x12\x00\x00\x00\x00\x00\x00\x00
