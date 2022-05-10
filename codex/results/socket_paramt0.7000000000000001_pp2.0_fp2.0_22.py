import socket
socket.if_indextoname(1)

iface_name = iface_names[0]

# Iface in use:
iface = net_ifaces[iface_name]

print(iface)

# Monitor mode:
iface.monitor()

# Re-scan interfaces
net_ifaces = pyric.interfaces()

# Monitor mode iface:
mon_iface = net_ifaces[iface_name]

# Create channel:
channel = pyric.channels(mon_iface)[0]
# To set a specific channel
# channel = pyric.channels(mon_iface)[0]

# Card info:
print(pyric.cardinfo(mon_iface))

# Card stats:
print(pyric.cardstats(mon_iface))

# Channel info:
print(pyric.channelinfo(mon_iface))

# Set the card in monitor mode:

# pyric.modeset(mon_iface, 'monitor')
print(pyric.modeset(mon_iface, 'monitor'))


