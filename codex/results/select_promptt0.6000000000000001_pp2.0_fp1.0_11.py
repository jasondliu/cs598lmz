import select
# Test select.select()
# Linux: platform: linux2
#        version: 2.7.2+
#        architecture: ('32bit', 'ELF')
#        machine: i686
#        processor: i686
#        uname: ('Linux', 'sol', '2.6.32-41-generic', '#94-Ubuntu SMP Fri Jul 6 18:56:31 UTC 2012', 'i686')

# Windows: platform: win32
#          version: 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)]
#          architecture: ('32bit', 'WindowsPE')
#          machine: AMD64
#          processor: AMD64 Family 16 Model 4 Stepping 2, AuthenticAMD
#          uname: ('Windows', 'PC01', '7', '6.1.7601', 'AMD64', 'Intel64 Family 6 Model 37 Stepping 5, GenuineIntel')

if platform.architecture()[0] == '32bit':
	import ctypes
	
	socket_t = ctypes.c_uint
elif platform
