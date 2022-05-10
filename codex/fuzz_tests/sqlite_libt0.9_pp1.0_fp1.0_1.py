import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

try:
    import unicornhat as unicorn
except:
    with open('/tmp/unicorn.log','w+') as f:
        f.write('Unicorn hat not imported.\n')
        f.write('\n')
        f.write('Getting path\n')
        f.write(os.path.dirname(__file__))
        f.write('\n')
        f.write('Probing sys.path...\n')
        for path in sys.path:
            f.write('{}\n'.format(path))
        f.write('\n')
    print('Unicorn hat should be in sys.path. A log is here: {}'.format(os.path.join(os.path.dirname(__file__),'/tmp/unicorn.log')))

#bluetooth
try:
    libbluetooth = ctypes.cdll.LoadLibrary(ctypes.util.find_library('bluetooth'))
except:
    with open('/tmp/unicorn.log','w+
