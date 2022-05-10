import socket
socket.if_indextoname(1)

raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
link_layer_addr = struct.pack('@I', int(hexlify(socket.inet_aton('localhost')), 16))
raw_socket.bind((link_layer_addr, socket.htons(0x0800)))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 0))

i_addr, i_port = s.getsockname()
print(i_addr, '= localhost')
print(i_port, '= port')

port = 1
# s.getsockname()[1]
while port != 0:
    message, client_addr = s.recvfrom(4096)
    count, message = message.split('\n')
    message, count = count[:-1], message.split(' ')
    print(message, count, client_addr)
    path = [i_addr]
