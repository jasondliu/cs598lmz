import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
        print "hahahahahahahahahaha"
sys.out.write('\x42\x42\x42\x42')
sys.out.write(FUNTYPE(fun))
sys.out.close()
