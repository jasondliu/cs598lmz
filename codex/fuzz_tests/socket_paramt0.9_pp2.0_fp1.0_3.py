import socket
socket.if_indextoname(socket.if_nametoindex(b'eth0'))

o_ehdr = struct.Struct('> H H 4x B B H H H 4x L')
def o_ether_header(buf,offset=0):
        return o_ehdr.unpack_from(buf,offset)

o_iphdr = struct.Struct('> B B H H 2x H B B H L L B B H')
def o_ip_header(buf,offset=0):
        return o_iphdr.unpack_from(buf,offset)

def parse_datagram(datagram):
        eth_header = o_ether_header(datagram,0)
        ipph_header = o_ip_header(datagram,14)
        ipd_header = o_ip_header(datagram,20)
        # combine into correct fields for output 
        return [format(x, '02x') for x in eth_header] +\
               [format(x, '02x') for x in ipph_header] +\
               [format(x, '
