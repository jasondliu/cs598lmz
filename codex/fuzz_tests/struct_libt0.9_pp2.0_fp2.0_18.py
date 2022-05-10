import _struct
    import _struct as struct

    # Prints the header of the SP packet, the IP header and payload
    def print_packet_header(ether):
        print('')
        print('Packet Header' + '-' * 60)
        print('Destination MAC: ', end='')
        print(mac_addr(ether.data.dst))
        print('Source MAC: ', end='')
        print(mac_addr(ether.data.src))
        print('Ether Type: ', ether.data.type, end=' ')
        print('')
        print('IP Header' + '-' * 60)
        # The IP header is located after the Ethernet header
        ip = ether.data
        return ip

    def tcp_flags(tcp):
        retflags = []
        if tcp.flags == 0:
            retflags.append('FIN')
        if tcp.flags == 1:
            retflags.append('SYN')
        if tcp.flags == 2:
            retflags.append('RST')
        if tcp.flags == 4:
            ret
