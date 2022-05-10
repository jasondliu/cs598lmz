import socket
socket.if_indextoname(3)

#add a function to get the default gateway
def get_default_gateway_linux():
    """Read the default gateway directly from /proc."""
    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                continue

            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))

def get_default_gateway_windows():
    """Read the default gateway directly from the registry."""
    import winreg
    gateway = ""
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    reg_key = winreg.OpenKey(reg, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters")
    for i in range(winreg.QueryInfoKey(reg_key)[1]):
        try:
            name, value, type = winreg.EnumValue(
