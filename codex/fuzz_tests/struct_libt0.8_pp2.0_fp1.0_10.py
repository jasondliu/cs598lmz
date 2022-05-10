import _struct
import ipaddress

# EIGRP packet types
TYPE_UPDATE = 0x01
TYPE_QUERY = 0x02
TYPE_REPLY = 0x03
TYPE_HELLO = 0x04
TYPE_IPXSAP = 0x05

# EIGRP K values
K_VALUE_BANDWIDTH = 0x0001
K_VALUE_LOAD = 0x0002
K_VALUE_DELAY = 0x0004
K_VALUE_RELIABILITY = 0x0008
K_VALUE_MTU = 0x0010

def get_k_values(flags):
    k_values = []
    if flags & K_VALUE_BANDWIDTH:
        k_values.append("K1-Bandwidth")
    if flags & K_VALUE_LOAD:
        k_values.append("K2-Load")
    if flags & K_VALUE_DELAY:
        k_values.append("K3-Delay")
    if flags & K_VALUE_RELIABILITY:
        k_values.append("K4-Reliability")

