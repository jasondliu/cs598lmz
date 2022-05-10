import socket
# Test socket.if_indextoname()
#
# (C)2019-2020, Laurent Pugin (lpugin@cloudflare.com)
#
# SPDX-License-Identifier: BSD-3-Clause

import sys
import subprocess

if __name__ == '__main__':
    # get list of interfaces
    proc = subprocess.Popen(['ifconfig', '-a'], stdout=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    ifaces = stdout.split(b'\n\n')
    if len(ifaces) == 0:
        print('No interfaces found')
        sys.exit(1)
    for iface in ifaces:
        lines = iface.split(b'\n')
        if len(lines) < 2:
            continue
        iface_name = lines[0].split(b':')[0].decode('utf-8')
        if iface_name.startswith('lo'):
            continue
