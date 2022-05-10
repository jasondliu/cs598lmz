import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.c_int,c_char_p)
def get_dns_config():
    try:
        import ctypes
        ppp_address = ctypes.windll.shell32.IsUserAnAdmin()
        if ppp_address == 0:
            return []
        dll = ctypes.windll.LoadLibrary("iphlpapi.dll")
        GetNetworkParams = dll.GetNetworkParams
        GetNetworkParams.restype = ctypes.c_ulong
        GetNetworkParams.argtypes = [ctypes.POINTER(FIXED_INFO),
                                     ctypes.POINTER(ctypes.c_ulong)]
        dwOutBufLen = ctypes.c_ulong()
        GetNetworkParams(None, ctypes.byref(dwOutBufLen))
        data_type = ctypes.c_char * dwOutBufLen.value
        data = data_type()
        res = GetNetworkParams(ctypes.byref(data), ctypes.byref(dwOutBufLen))

