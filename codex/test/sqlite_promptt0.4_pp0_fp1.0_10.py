import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/pi/Desktop/Thingy.db")

# Some constants used to ioctl the device file. I got them by a simple C
# program.
USBDEVFS_RESET = 21780
USBDEVFS_CONNECT = 21800
USBDEVFS_DISCONNECT = 21801
USBDEVFS_CLAIMINTERFACE = 21503
USBDEVFS_RELEASEINTERFACE = 21504

# This is the path to the usb device file.
USBDEV = "/dev/bus/usb/001/002"

# Open the file in read/write mode
usbfs = os.open(USBDEV, os.O_RDWR)

# Send an ioctl to the device file. The parameter is ignored for USBDEVFS_RESET.
ret = fcntl.ioctl(usbfs, USBDEVFS_RESET, 0)

# Send an ioctl to the device file.
ret = fcntl.ioctl(usbfs, USBDEVFS_CONNECT, 0)

# Send an ioctl to the device file.
