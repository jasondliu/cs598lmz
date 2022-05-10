import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long)

def myfunc(name, addr, status):
	print name, addr
	print status

pncclient.c_initialize()
pncclient.c_registerCallback(FUNTYPE(myfunc))

while True:
	data = raw_input()
	data = data.split()
	if(len(data)<2):
		print "Enter instructor name and id"
		continue
	print pncclient.c_regInstructor(data[0], data[1])

pncclient.c_cleanup()
