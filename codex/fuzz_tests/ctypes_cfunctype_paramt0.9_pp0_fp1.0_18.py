import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool, *(ctypes.POINTER(globals.WinStructure), ctypes.POINTER(globals.DeviceTypedef), ctypes.POINTER(globals.PacketTypedef), ctypes.c_uint, ctypes.c_void_p), )
def dispatch(window, device, packet, size, ancdata):
    """
    Callback function for a window event.

    Use it to separate user code from the underlying library.

    Parameters:
        window (globals.WinStructure): the window structure (from C)
        device (globals.DeviceTypedef): the device structure (from C)
        packet (globals.PackeetTypedef): the packet
        size (int): the packet size
        ancdata (ctypes.voidp): private parameter

        See libasound documentation for more details
    """
    # print(window, device, packet, size, ancdata)
    print('hi there!')
    return False
# end of dispatch

def push_scheduled(arg):

