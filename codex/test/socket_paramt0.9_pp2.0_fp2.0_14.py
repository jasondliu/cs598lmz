import socket
socket.if_indextoname(18)

import subprocess
subprocess.check_output("ifconfig eth0 | grep inet", shell=True)

import os
os.system("/usr/bin/python dist/scripts/spoof_dhcp_request.py")

import sys
sys.executable

import sys
#import readline
#sys.path.insert(0, os.environ['HOME']+'/.pystartup')
#readline.read_init_file(os.environ['HOME']+'/.pystartup')
#readline.read_history_file(os.environ['HOME']+'/.pyhistory')
#readline.parse_and_bind("tab: complete")


# mac address
def get_mac(iface):
    from uuid import getnode
    import uuid
    str = ""
    for octet in uuid.uuid1().hex:
        str += octet.__str__()
