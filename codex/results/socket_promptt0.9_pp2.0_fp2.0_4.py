import socket
# Test socket.if_indextoname works on a simple case.
if_indextoname(socket.if_nametoindex(interface[2]))
# Running netifaces.interfaces() makes netifaces.ifaddresses() work.
netifaces.interfaces()
netifaces.ifaddresses(interface[2])
netifaces.ifaddresses(interface[2])[netifaces.AF_INET]
netifaces.ifaddresses(interface[2])[netifaces.AF_INET][0]['addr']
netifaces.gateways()
netifaces.gateways()["default"][netifaces.AF_INET]
netifaces.gateways()["default"][netifaces.AF_INET][0]
netifaces.gateways()["default"][netifaces.AF_INET][1]
netifaces.gateways()["default"][netifaces.AF_INET][2]

# Try a test case where the interface doesn't exist on the machine,
# such as interface[1]
try:
    if_indextoname(
