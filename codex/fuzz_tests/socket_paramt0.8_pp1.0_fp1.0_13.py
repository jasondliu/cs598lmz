import socket
socket.if_indextoname(int(args.interface))

print('\n  Creating IP Raw socket')
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

print('\n  Setting socket options')
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, args.interface)

print('\n  Sending packets')
if (args.destination != 'ip') and (args.destination != 'mac'):
    print('     Send to %s %d packets' % (args.destination, args.count))
    s.sendto(packet, (args.destination, 0))
else:
    count = 0
    while (count < args.count):
        print('     Send to %s %d packets' % (args.destination, count))
