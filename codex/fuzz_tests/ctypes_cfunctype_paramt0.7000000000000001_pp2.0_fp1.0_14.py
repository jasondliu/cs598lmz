import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

import contextlib


@contextlib.contextmanager
def pybluez_guard():
    try:
        yield
    except RuntimeError as e:
        if e.args[0] == 'Bluetooth Error: Not connected':
            print('not connected')
        elif e.args[0] == 'Bluetooth Error: Operation already in progress':
            print('already in progress')
        else:
            raise e

# import json

# with open('/sys/class/bluetooth/hci0/address', 'r') as f:
#     laddr = f.readline().strip()

# with open('/sys/class/bluetooth/hci0/name', 'r') as f:
#     lname = f.readline().strip()

# with open('/sys/class/bluetooth/hci0/revision', 'r') as f:
#     lrevision = f.readline().strip()

# with open('/sys/class/bluetooth/hci0/manufacturer', 'r') as f
