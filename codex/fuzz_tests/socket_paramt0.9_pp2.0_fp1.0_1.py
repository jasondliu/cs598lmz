import socket
socket.if_indextoname(data['interface'])

# Function to recieve packets asynchronously and when the receiving thread terminates print the summary statistics.
def record_data(conn):
	# Initialize the variables for summary statistics.
	total_packets = 0
	total_headers = 0
	ips = dict()
	protocols = dict()
	ports = dict()
	largest_packet = (0,0)
	smallest_packet = (sys.maxsize,0)

	# Receive packets
	while True:
		# Recieve data in small chunks of 64 bytes
		try:
			data = conn.recv(2**16)
			if data == '':
				break

			# Update summary statistics
			total_packets += 1
			total_headers += (len(data) + 14)/64
			if len(data) > largest_packet[0]:
				largest_packet = (len(data),total_packets)
			if len(data) < smallest_packet
