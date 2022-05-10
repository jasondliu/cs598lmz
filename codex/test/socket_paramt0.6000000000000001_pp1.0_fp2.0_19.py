import socket
socket.if_indextoname(1)

# to change the name of an interface
import netifaces
netifaces.if_setifname(1, "eth2")

# get the index of an interface
netifaces.if_nametoindex("eth2")

# get the MAC address of an interface
netifaces.ifaddresses("eth2")[netifaces.AF_LINK][0]["addr"]

# get the inet address of an interface
netifaces.ifaddresses("eth2")[netifaces.AF_INET][0]["addr"]

# get the index of the default interface
netifaces.gateways()["default"][netifaces.AF_INET][1]

# get the name of the default interface
netifaces.gateways()["default"][netifaces.AF_INET][0]

# get the name of the default interface
netifaces.gateways()["default"][netifaces.AF_INET][0]

# get the name of the default interface
