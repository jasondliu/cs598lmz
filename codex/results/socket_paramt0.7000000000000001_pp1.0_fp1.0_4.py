import socket
socket.if_indextoname(socket.if_nametoindex('wlan0'))

# Now we need to create an interface object

iface = Interface('wlan0')
iface

# iface is a new object that has all the methods associated with the 'Interface' class to use on the wlan0 interface

# If we want to see which attributes and methods we can use for this type of class we can use the 'dir()' function

dir(iface)

# We can also use the 'help()' function to see a brief summary of the methods

help(iface)

# We can find out what the methods do by looking at them in the source code.
# The source code for the library is stored on GitHub: https://github.com/kamakazikamikaze/wifi
# We can see the code for the Interface class stored in: https://github.com/kamakazikamikaze/wifi/blob/master/wifi/scan.py

# We can see what all the methods do by looking at the source code in the scan.py file

# For example we can use
