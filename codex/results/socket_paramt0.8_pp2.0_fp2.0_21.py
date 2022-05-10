import socket
socket.if_indextoname(3)

# Updating the interface name to match the current index
interface = "enp0s3"

# Updating the IP address to match the current IP address
ip_address = "192.168.1.10"

# Initialize the socket
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)

# Bind the socket to the interface and IP address
s.bind((interface, 0))

# Create a message that can be sent to the broadcast IP address
message = "Hello Broadcast World"

# Set the destination MAC address and fill in the IP header
destination_mac = "\xff\xff\xff\xff\xff\xff"
ip_header = "4500001c0001000040060000c0a80101c0a8010a"

# Calculate the checksum of the IP header
checksum = ip_checksum(ip_header)

# Create the final IP header with the checksum
ip_header = "4500001c0001000040060000c0a80101c0a8010a" + checksum


