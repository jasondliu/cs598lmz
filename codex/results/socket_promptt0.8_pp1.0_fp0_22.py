import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

print('Parse Packet...')
pkt = sniff(count=1)

print(pkt)
print(type(pkt))
print(type(pkt[0]))
print(pkt[0].show())
print(repr(pkt[0]))
