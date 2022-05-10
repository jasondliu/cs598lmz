import _struct
# Test _struct.Struct, different times for alignment, little and big endian
# and standard sizes
#
# _struct.Struct should have fixed/specified/deterministic size/NF.
# (i.e. n of number of floats)

if __name__ == "__main__":
    import os
    import sys
    import numpy as np
    import time

    t_struct = _struct.Struct('d'*10)

    align = 4

    size = 4*10

    fname = 'test_struct_times_al%d_sz_%d_%s.bin'%(align,size,sys.byteorder)

    fh = open(fname,'wb')
    t0 = time.time()
    fh.write(t_struct.pack(*(t0,)*10))
    fh.close()




    fh = open(fname,'rb')
    buf = fh.read()
    xs = t_struct.unpack(buf)
    print(xs)

    t1 = time.time()

