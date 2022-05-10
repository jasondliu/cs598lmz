import socket
socket.if_indextoname(1)

#get the MAC address of an interface
import uuid
mac1 = uuid.getnode()
mac2 = hex(uuid.getnode())
mac3 = ':'.join(("%012X" % mac1)[i:i+2] for i in range(0, 12, 2))

#get the MAC address of the computer
import getmac
getmac.get_mac_address()

#get the MAC address of the computer
import uuid
mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
mac = ":".join([mac[e:e+2] for e in range(0,11,2)])

#get the MAC address of the computer
import uuid
mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
mac = ":".join([mac[e:e+2] for e in range(0,11,2)])

#get the MAC address of the computer
import uuid
