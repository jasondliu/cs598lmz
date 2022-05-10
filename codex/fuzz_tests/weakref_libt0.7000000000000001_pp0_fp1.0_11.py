import weakref

from src.core.core import PyCore
from src.core.coreobj import PyCoreObj

class PyCoreNetIf(PyCoreObj):
    """
    A network interface object.

    This class represents a network interface object.
    """
    def __init__(self, session, objid = None, name = None, verbose = True,
                 starttime = None, duration = None, lo = None,
                 lo_ip4 = None, lo_ip6 = None, lo_ip6_prefix = 64,
                 lo_ip4_prefix = 24, lo_ip6_linklocal = None,
                 lo_ip6_linklocal_prefix = 64):
        """
        Create a new network interface object.

        @param session: a session object.
        @type session: L{Session}
        @param objid: internal object ID.
        @type objid: C{int}
        @param name: network interface name (e.g., "eth0", "tap0", "wlan0")
        @type name: C{str}
        @param verbose
