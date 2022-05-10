import socket
socket.if_indextoname(3)

# Edit the file to add the entry below.
# The line should look like so:
# 1c:6f:65:0f:4d:b2  enx1c6f650f4db2
# Then you can use dnsmasq (configured to support dhcp)
# to assign a static ip address to the device, based on the mac address
