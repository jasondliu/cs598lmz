import socket
socket.if_indextoname(2)

def list_devices():
    # List all devices
    nics = []
    info = psutil.net_if_addrs()
    for k, v in info.items():
        for item in v:
            if item[0] == 2 and not item[1] == '127.0.0.1':
                nics.append((k, item[1]))
    return nics

n = list_devices()
print(n)
