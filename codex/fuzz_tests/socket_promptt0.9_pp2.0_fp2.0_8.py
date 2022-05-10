import socket
# Test socket.if_indextoname()
print 'Interface name', socket.if_indextoname(1)
# Indicate we are using the OpenFlow 1.0 protocol
OF_P_OF_10 = 0x1
# Create a test packet
pkt = simple_tcp_packet()
def make_pkt(addr, rltv, flags, seq_num, ack_num,
             win_size, c_sum, cntr):
    # Use the function hack library to create this packet
    # 4(*4+4)+(4+4)+(4+4)+(4+4+2+2)+(4+4)
    # Options need to be accepted in host byte order
    pkt = funcnt_fuzz_packet(pkt, addr, rltv, flags, seq_num, ack_num,\
    win_size, c_sum, cntr)
    return pkt
# Function needs a dummy arg to generate a random IP address
def gen_ip_random(dummy):
    return 32, 32, 32, 32
# Create a list of the potential values the
