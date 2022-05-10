import socket
socket.if_indextoname(2)
#'eth0'

# if_indextoname(index)
# Return the interface name for the given integer index.

# if_nameindex()
# Return a list of tuples (index, name) for all interfaces.

# if_nametoindex(name)
# Return the integer index for the given interface name.

# Interface names and indexes can be used with the SIOCGIF* ioctl calls
# to retrieve interface info.
#
# The following example uses the if_nameindex() function to print a list
# of all interfaces and their indexes:

import socket
for i, name in socket.if_nameindex():
    print(i, name)
#1 lo
#2 eth0
#3 eth1
#4 wlan0
#5 wlan1
#6 vboxnet0
#7 vboxnet1
#8 vboxnet2
#9 vboxnet3
#10 vboxnet4
#11 vboxnet5
#12 vboxnet6
#13 vboxnet7
#14 vboxnet8
#15 vboxnet
