import socket, sys
+from struct import *
+
+try:
+	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
+except socket.error, msg:
+	print "Socket could not be created. Error Code: " + str(msg[0]) + " Message " + msg[1]
+	sys.exit()
+
+while True:
+	packet = s.recvfrom(65565)
+	packet = packet[0]
+	eth_length = 14
+	eth_header = packet[:eth_length]
+	eth = unpack('!6s6sH', eth_header)
+	eth_protocol = socket.ntohs(eth[2])
+	print 'Destination MAC: ' + eth_addr(packet[0:6]) + ' Source MAC: ' + eth_addr(packet[6:12]) + ' Protocol: ' + str(eth_protocol)

