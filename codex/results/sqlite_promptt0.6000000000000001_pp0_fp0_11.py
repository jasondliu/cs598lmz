import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/var/lib/libvirt/images/test.img')

# We can find the libvirt library in several different places
# depending on the operating system, so ask ctypes.util to tell us
# where it is.
if sys.platform == 'darwin':
    libvirt = ctypes.cdll.LoadLibrary('libvirt.dylib')
else:
    libvirt = ctypes.cdll.LoadLibrary(ctypes.util.find_library('virt'))

VIR_DOMAIN_NOSTATE = 0
VIR_DOMAIN_RUNNING = 1
VIR_DOMAIN_BLOCKED = 2
VIR_DOMAIN_PAUSED = 3
VIR_DOMAIN_SHUTDOWN = 4
VIR_DOMAIN_SHUTOFF = 5
VIR_DOMAIN_CRASHED = 6
VIR_DOMAIN_PMSUSPENDED = 7

VIR_DOMAIN_XML_SECURE = 1 << 0    # Dump security sensitive information too
VIR_DOMAIN_XML_INACTIVE = 1 << 1  # Dump
