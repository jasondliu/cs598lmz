import socket
# Test socket.if_indextoname()

if_indextoname = socket.if_indextoname

# On Windows, we can't use the loopback interface, because it's not
# always available.  So we use the first non-loopback interface.
if sys.platform == 'win32':
    import win32api
    import win32con
    import pywintypes
    import win32net

    # Get the interface index of the first non-loopback interface.
    def if_indextoname(index):
        try:
            return win32net.GetInterfaceInfo(index,
                                             win32con.MIB_IF_TYPE_OTHER)[0]
        except pywintypes.error:
            raise ValueError("invalid interface index")

    # Get the index of the first non-loopback interface.
    def get_non_loopback_index():
        for index in range(8):
            try:
                name = if_indextoname(index)
            except ValueError:
                continue
            if name != 'lo':
                return index
        raise ValueError("no
