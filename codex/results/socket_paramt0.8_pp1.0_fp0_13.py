import socket
socket.if_indextoname(3)

# Edit the file to add the entry below.
# The line should look like so:
# 1c:6f:65:0f:4d:b2  enx1c6f650f4db2
# Then you can use dnsmasq (configured to support dhcp)
# to assign a static ip address to the device, based on the mac address
sudo nano /etc/ethers

# Find out which interface the controller is running on.
ip tuntap
# This command should output 'tap0' if the contactor is running in a vm
# and 'tun0' if the controller is running on a raspberry pi or similar device
# If you are running the controller on a physical machine, replace 'tap0'
# with the name of the interface you wish to run the controller on
sudo ip tuntap add dev tap0 mode tap user root
ip link set dev tap0 up
ip addr add 10.10.10.1/24 dev tap0
sudo ip tuntap del dev tap0 mode tap

# Create a file called /usr/local/bin/start_controller.sh

