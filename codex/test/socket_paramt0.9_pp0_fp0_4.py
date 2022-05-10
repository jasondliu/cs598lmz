import socket
socket.if_indextoname("0")

# 'eth0'

# Now, we can just print out the present IP addresses on this port:

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

# to access other tools that are also installed on your router:

# import os
# os.system("curl ifconfig.me")

# other software tools include Traceroute and Ping

# Remember: a packet is just your message enclosed within an IP
# address which is the “From” address and the IP address of its
# intended recipient which is the “To” address.

# a packet is a message that you’re sending somewhere, it’s
# just data.

# Section 16.3 is a description of the Ethernet Frame
# Section 16.4 is a description of the IP Packet, including IP
# address structure, min/max lengths and field sizes

# there’s nothing to join except for the physical wires you
