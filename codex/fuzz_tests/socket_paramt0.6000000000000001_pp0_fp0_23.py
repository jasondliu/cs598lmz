import socket
socket.if_indextoname(1)

#methods for converting IP addresses to binary format

#hexadecimal representation
'{:02x}'.format(255)

#decimal representation
'{:08b}'.format(255)

#convert ip to binary
'{:08b}.{:08b}.{:08b}.{:08b}'.format(*'192.168.1.1'.split('.'))

#convert ip to decimal
'{}.{}.{}.{}'.format(*'11000000.10101000.00000001.00000001'.split('.'))

#convert ip to hexadecimal
'{:02x}.{:02x}.{:02x}.{:02x}'.format(*'192.168.1.1'.split('.'))
