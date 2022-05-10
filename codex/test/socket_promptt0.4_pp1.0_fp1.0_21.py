import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform == "win32":
    import os
    import subprocess
    import time

    # Create a temporary loopback interface
    if os.name == "nt":
        subprocess.check_call(["netsh", "interface", "ipv4", "add", "loopback", "loopback=enabled", "address=127.0.0.1", "mask=255.255.255.0"])
    else:
        subprocess.check_call(["netsh", "interface", "ipv4", "add", "loopback", "loopback=enabled", "address=127.0.0.1", "mask=255.255.255.0"])
    time.sleep(1)

if_index = socket.if_nametoindex('loopback')
if_name = socket.if_indextoname(if_index)

print('if_index:', if_index)
print('if_name:', if_name)

