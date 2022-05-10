import socket
socket.if_indextoname('8')

socket.if_nametoindex('en0')

#在计算机上所有可用的网络接口列表
for interface_name in sorted(netifaces.interfaces()):
    addrs = netifaces.ifaddresses(interface_name)
    print('\n*** interface:', interface_name)
    for family in addrs.keys():
        print('  Address family:', family)
        for ip_addr in addrs[family]:
            print('    IP address  :', ip_addr['addr'])
            if 'broadcast' in ip_addr:
                print('    Broadcast   :', ip_addr['broadcast'])
            if 'netmask' in ip_addr:
                print('    Netmask     :', ip_addr['netmask'])
            if 'peer' in ip_addr:
                print('    Peer        :', ip_addr['peer'])

