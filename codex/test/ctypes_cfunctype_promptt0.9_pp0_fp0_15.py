import ctypes
# Test ctypes.CFUNCTYPE()
def int_array_to_chr_array(int_array):
    return ''.join(map(chr, int_array))
