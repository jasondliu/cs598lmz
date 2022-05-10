import socket
socket.if_indextoname(1)

try:
    import winreg as _winreg
except ImportError:
    # winreg module does not exist on Python 3
    _winreg = None

import scapy.config
import scapy.route

# IP_ADAPTER_ADDRESSES structure
# http://msdn.microsoft.com/en-us/library/windows/desktop/aa366058%28v=vs.85%29.aspx
class IP_ADAPTER_ADDRESSES(Structure):
    """
    IP_ADAPTER_ADDRESSES structure
    """
    _fields_ = [
        ("length", c_ulong),
        ("if_index", c_uint),
        ("next", c_ulong),
        ("adapter_name", POINTER(c_char)),
        ("first_unicast_address", POINTER(IP_ADAPTER_UNICAST_ADDRESS)),
        ("first_anycast_address", POINTER(IP_ADAPTER_ANYCAST_ADDRESS)),
        ("first_multicast_address", POINTER(IP_AD
