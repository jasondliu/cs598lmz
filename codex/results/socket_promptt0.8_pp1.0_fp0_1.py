import socket
# Test socket.if_indextoname
#
# This uses a 1-second timeout, which means it has to be run with a network
# interface up, or it will timeout for that reason.
#
# (c) 2011 Chris Webb <chris@arachsys.com>
# Released under the same terms as BusyBox itself.

import os
import sys
import subprocess

if len(sys.argv) != 2:
    print("Usage: if_indextoname.py <ifname>")
    sys.exit(1)

ifname = sys.argv[1]

# make sure the interface exists
if not os.path.exists("/sys/class/net/%s" % ifname):
    print("Error: interface %s does not exist" % ifname)
    sys.exit(1)

# make sure the interface is up
proc = subprocess.Popen(["ip", "link", "show", "up", ifname],
        stdout=subprocess.PIPE, stderr=subprocess.STDERR)
proc.communicate()
if proc.returncode
