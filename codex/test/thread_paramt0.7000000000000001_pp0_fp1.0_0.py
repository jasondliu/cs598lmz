import sys, threading
threading.Thread(target=lambda:sys.stdout.write("Hello world\n")).start()

# System information
import platform
print(platform.python_version())
print(platform.platform())
print(platform.system())
print(platform.release())

# Number formats
print('{:010d}'.format(42))
print('{:.2f}'.format(3.141592653589793))
print('{:f}'.format(3.141592653589793))
print('{:e}'.format(3.141592653589793))
print('{:.2e}'.format(3.141592653589793))
print('{:.2e}'.format(3.141592653589793))
print('%04d' % 42)
print('%.2f' % 3.141592653589793)
print('%e' % 3.141592653589793)
print('%E' % 3.141592653589793)

# Testing strings
import re
def is_valid_uuid(uuid):
    return re
