import io
# Test io.RawIOBase as return from cl.to_buffer.

def check_sequence(bs):
    """
    Check that each b[i] is equal to i (modulus 256).
    
    >>> check_sequence(b"Hello World!")
    True
    
    """
    seq = list(bs)
    return all(i == v % 256 for i,v in enumerate(seq))

def test(buffer_factory=bytearray):
    """
    Run the test.
    
    >>> test()
    True
    >>> test(str)
    True
    
    """
    import cl
    
    dev = cl.clGetDeviceIDs()[0]    
    platform = dev.platform
    ctx = cl.clCreateContext([platform], [dev])
    queue = cl.clCreateCommandQueue(ctx, dev)
    
    cl_options = "-cl-mad-enable"

    for wkgrpsz_log2 in range(4, 16, 4):
        wkgrpsz = 1 << wkgrpsz_log2
