import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def _(func):
    return (FUNTYPE(func))

#
#   Initialize the library
#

#
#   Initialize the library
#

def initialize(options):
    if options.debug:
        _lib.BACnet_debug = 1
    else:
        _lib.BACnet_debug = 0

    if options.debug_addr:
        _lib.BACnet_debug_addr = 1
    else:
        _lib.BACnet_debug_addr = 0

    if options.debug_asn1:
        _lib.BACnet_debug_asn1 = 1
    else:
        _lib.BACnet_debug_asn1 = 0

    if options.debug_aps:
        _lib.BACnet_debug_aps = 1
    else:
        _lib.BACnet_debug_aps = 0

    if options.debug_bvlc:
        _lib.BACnet_debug_bvlc = 1
    else:
        _lib.BACnet_debug_
