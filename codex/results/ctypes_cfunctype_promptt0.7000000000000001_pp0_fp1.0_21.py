import ctypes
# Test ctypes.CFUNCTYPE?

# Load and parse
#
# Load the driver.
print "Loading driver..."
d = ctypes.WinDLL(r"C:\Program Files (x86)\Exodriver\Exodriver\bin\exodriver.dll")
# Load the library.
print "Loading library..."
l = ctypes.WinDLL(r"C:\Program Files (x86)\Exodriver\Exodriver\bin\labjackusb.dll")
# Get the device count.
print "Getting device count..."
count_func = l.LJUSB_GetDevCount
count_func.restype = ctypes.c_long
count = count_func(0x5f9)
print "Device count: " + str(count)

# Open a device.
print "Opening device..."
open_func = l.LJUSB_OpenDevice
open_func.restype = ctypes.c_long
handle = open_func(1, 0, 0x5f9)
print "Handle: " + str(handle)

# Close the device.
print "Closing device..."

