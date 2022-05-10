import _struct

class Packet:
    def __init__(self, data, ip_header, protocol, udp_header, tcp_header):
        self.data = data
        self.ip_header = ip_header
        self.protocol = protocol
        self.udp_header = udp_header
        self.tcp_header = tcp_header
        self.version = ip_header[0] >> 4
        self.header_length = (ip_header[0] & 0x0f) * 4
        self.total_length = ip_header[2]
        self.ttl = ip_header[5]
        self.src_ip = socket.inet_ntoa(ip_header[8])
        self.dst_ip = socket.inet_ntoa(ip_header[9])

        if self.protocol == socket.IPPROTO_TCP:
            self.src_port = tcp_header[0]
            self.dst_port = tcp_header[1]
            self.seq_num = tcp_header[2]
            self.ack
