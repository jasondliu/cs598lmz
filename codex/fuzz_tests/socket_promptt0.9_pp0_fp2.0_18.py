import socket
# Test socket.if_indextoname
flowlabel = 0
ttl = 255
proto = socket.IPPROTO_IPV6

for ipv6_idx in range(0, 32):
    print "====================="
    print "index:", ipv6_idx
    ipv6_addr = socket.if_indextoname(ipv6_idx)
    if ipv6_addr is None:
        print "Example!!!:", ipv6_idx, " is a wrong index!!!"
    else:
        print ipv6_addr
        (src_addr, dst_addr) = utils.get_addresses(ipv6_addr, address_type='IPv6')
        src_addr = [src_addr[0].replace('-', ':'), src_addr[1]]
        if (dst_addr[0] == ''):
            dst_addr = src_addr

        print "source:", src_addr
        print "dest  :", dst_addr

        # Get pcap file from capture_result based on host_ip, device ip and proto

