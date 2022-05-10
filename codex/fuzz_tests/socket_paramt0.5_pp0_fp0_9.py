import socket
socket.if_indextoname(1)

# Returns the MAC address as a string, e.g. '00:1f:e1:dd:08:3d'
import uuid
uuid.getnode()

# Returns the MAC address as an integer, e.g. 2130706433
import uuid
uuid.getnode()

# Returns the MAC address as a string, e.g. '00:1f:e1:dd:08:3d'
import uuid
hex(uuid.getnode()).replace('0x', '').replace('L', '')

# Returns the MAC address as a string, e.g. '00:1f:e1:dd:08:3d'
import uuid
':'.join(('%012x' % uuid.getnode())[i:i+2] for i in range(0, 12, 2))

# Returns the MAC address as a string, e.g. '00:1f:e1:dd:08:3d'
import netifaces
mac = netifaces.ifaddresses('eth0')[net
