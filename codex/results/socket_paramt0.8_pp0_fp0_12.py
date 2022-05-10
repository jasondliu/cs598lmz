import socket
socket.if_indextoname(1)

# These numbers can be found in /sys/class/net
# each entry will have a symlink to the device and a symlink to the
# parent device.

# or better yet, use the udevadm command, which will print out all the device
# names and their numbers

# or even better, use the ifconfig command on the command line and this
# will print out all the device names and numbers

# or even better yet, use the netifaces module, which we will talk about
# in the next section
