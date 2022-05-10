import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

#~ def CallBack(arg):
    #~ val = arg[0]
    #~ print "val=",val
    #~ print "arg=",arg
    #~ return val

#~ lib = ctypes.CDLL("libsimFunc.so")
#~ cbf = FUNTYPE(CallBack)

#~ lib.my_func(np.ctypeslib.as_ctypes(np.array(data, dtype=np.int32)), cbf)
#~ print '-----result------'
#~ print data

#--------------------------------------sortir ci-dessous
