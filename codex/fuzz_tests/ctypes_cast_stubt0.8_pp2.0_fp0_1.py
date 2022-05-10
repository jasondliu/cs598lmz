import ctypes
ctypes.cast(lltype.nullptr(rffi.VOIDP.TO), lltype.Signed)

# ____________________________________________________________
# create a buffer and fill it with raw data

SIZE = 8

def test_fill_raw_buffer():
    buf = lltype.malloc(rffi.CCHARP.TO, SIZE, flavor='raw')
    for i in range(SIZE):
        buf[i] = 'A'
    for i in range(SIZE):
        assert buf[i] == 'A'
    lltype.free(buf, flavor='raw')

# ____________________________________________________________
# allocate an array

def test_allocate_array():
    buf = lltype.malloc(rffi.CCHARPP.TO, 2, flavor='raw')
    buf[0] = lltype.nullptr(rffi.CCHARP.TO)
    buf[1] = lltype.malloc(rffi.CCHARP.TO, SIZE, flavor='raw')
    for i in range(SIZE):
        buf[1][i] = '
