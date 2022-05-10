from _struct import Struct
s = Struct.__new__(Struct) # Hack for python 3.4
s.format = '4s4s'
s.size = 8
s.pack_into(buffer, 0, b'\x01\x02\x03\x04', b'\x05\x06\x07\x08')

# First we need to create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Now we need to bind it to the right address and port
sock.bind((MCAST_GRP, MCAST_PORT))

# And then join the multicast group
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Now just listen for the data to come in
while True:
    data, addr = sock.recvfrom(1024)
    print("Got data from", addr)
   
