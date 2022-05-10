import socket
socket.if_indextoname(3)
sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
sock.bind(('eth0', socket.htons(0x0800)))
sock.recvfrom(65565)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
sock.sendto('hello world'.encode(), (dest_ip, 0))

# https://gist.github.com/pklaus/856268
def parse_ethernet(data):
    (dst, src, proto), data = struct.unpack('6s6sH', data[:14]), data[14:]
    return (macbin_to_str(dst), macbin_to_str(src), socket.htons(proto)), data
def parse_ip_datagram(data):
    (ver_ihl, tos, tot_len, id, frag_off, ttl, proto, checksum, src, dst) = struct.unpack
