import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_void_p,ctypes.c_void_p)
dfn=FUNTYPE(do_noise)
def c_do_noise(m,noise):
    ptr=m.gauss.ctypes.data_as(ctypes.c_void_p)  #We pass pointers to the data
    ptr2=noise.ctypes.data_as(ctypes.c_void_p)
    r=dfn(m.n,ptr,ptr2)
    return r
noise=numpy.array(numpy.random.rand(1)[0],dtype=numpy.float64)
c_do_noise(m,noise)

pl.imshow(m.gauss,interpolation='nearest',vmin=0,vmax=1,
                                                                    cmap=pl.cm.Greys_r)
s=numpy.sum(m.gauss)
print s

c_do_noise(m,3.0)

