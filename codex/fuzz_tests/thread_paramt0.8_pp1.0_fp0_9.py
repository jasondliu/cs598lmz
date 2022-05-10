import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\x07')).start()
!python3 -c "import threading ; threading.Thread(target=lambda:print('\x07')).start()"
import os
os.system('\a')

# Other cross-platform solutions
# ...
</code>

On the other hand, if you want a standalone script to run in the background, and want to receive the beep remotely:
<code>#!/usr/bin/env python

import socket, threading, subprocess, sys

def send_beep(host='localhost', port=4001):
    try:
        s = socket.create_connection((host, port), timeout=5)
        s.close()
    except:
        pass

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s host' % sys.argv[0])
    else:
        t = threading.Thread(target=send_beep, args=(sys.argv[1],))
        t.daemon = True
