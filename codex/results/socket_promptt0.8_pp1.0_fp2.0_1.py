import socket
# Test socket.if_indextoname
# This is used in the address specification (for binding and connecting)
# to refer to a local interface.
#
# Tests covers the basic functionality.
#
# The test works in two passes.  The first pass looks up the
# names of the interfaces and creates a set of tuples of the form
# (if_name, if_index, is_loopback), where if_name is the name
# of the interface, if_index is the index of the interface and
# loopback is either True if the interface is loopback, or False
# if it is not.
#
# The second pass checks that the name returned by socket.if_indextoname
# is in the set of names for the local machine, that is, that the
# interface is in fact a local interface.
ntuple = namedtuple('ntuple', 'if_name if_index is_loopback')

def _get_if_index():
    """
    Helper function that returns a set of tuples.
    """
    set_ = set()
    for i in range(100):
        try:
            ifname
