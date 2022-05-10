import socket
# Test socket.if_indextoname()
#
#  0 - lo
#  1 - eth0
#  2 - eth1
#
# Port numbers (socket.htons())
#
# eth0 - 80
# eth1 - 81
#
ifIndexes = []
ifIndexes.append(0)
ifIndexes.append(1)
ifIndexes.append(2)
portNumbers = []
portNumbers.append(socket.htons(80))
portNumbers.append(socket.htons(81))
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
for ifIndex in ifIndexes:
    for portNumber in portNumbers:
        try:
            print ifIndex, socket.if_indextoname(ifIndex), portNumber, socket.getservbyport(portNumber)
            s.bind((socket.if_indextoname(ifIndex), portNumber))
        except socket.error as e:
            print "Error: ", e
        except socket.gaierror as e:
            print "Error: ", e
</code>

