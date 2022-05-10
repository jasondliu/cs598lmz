import socket
socket.if_indextoname(3)

#import array
#import fcntl
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#max_possible = 8 # initial value
#while True:
#    bytes = max_possible * 32
#    names = array.array('B', '\0' * bytes)
#    outbytes = struct.unpack('iL', fcntl.ioctl(
#        s.fileno(),
#        0x8912,  # SIOCGIFCONF
#        struct.pack('iL', bytes, names.buffer_info()[0])
#    ))[0]
#    if outbytes == bytes:
#        max_possible *= 2
#    else:
#        break
#namestr = names.tostring()
#interface_names = [namestr[i:i+32].split('\0', 1)[0] for i in range(0, outbytes, 32)]
#print interface_names
import socket
import struct

