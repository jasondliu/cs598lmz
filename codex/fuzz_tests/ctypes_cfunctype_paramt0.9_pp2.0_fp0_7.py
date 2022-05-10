import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

with open(dest_file, 'wb') as f:
    f.write(prog.encode('utf-8'))

mod = SourceModule(prog)
ker = mod.get_function("kernel_code")
ker.prepare("PPP")

x, y, z= *[np.arange(10, dtype=np.float64) for _ in range(3)],
    
ker(cuda.InOut(x), cuda.InOut(y), cuda.InOut(z),
    block=(10,1,1), grid=(100,1))
</code>

