import socket
socket.if_indextoname(4)
#'Wi-Fi'

#Enumerate the interfaces on a system

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

max_possible = 128
_bytes = max_possible*32
names = array.array('B', b'\0'*_bytes)
outbytes = struct.unpack('iL', fcntl.ioctl(
    s.fileno(),
    0x8912,
    struct.pack('iL', _bytes, names.buffer_info()[0])
))[0]

'''
The wordsize of the addresses is always 32, so each interface needs 32/8=4 bytes.
The first four bytes are an integer number of the interface. The remaining 28 bytes are the actual name, meaning that the answer to the original question may be something like 
'eth0\x00\x00\x00\x00'
'''

nics = [names[i:i+32].tostring().split('\0', 1)[0] for i in range(0,
