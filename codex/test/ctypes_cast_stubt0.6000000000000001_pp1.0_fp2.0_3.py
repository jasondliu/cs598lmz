import ctypes
ctypes.cast(1, ctypes.py_object)

# Src: http://stackoverflow.com/questions/3488934/simple-way-to-convert-int-to-binary-in-python
def int_to_bin(i):
    if i == 0: return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i /= 2
    return s

class Convertor:
    """
    Converts a decimal number to any given base
    """
    def __init__(self):
        self.convertor = {}
        self.convertor[2] = self.to_binary
        self.convertor[8] = self.to_octal
        self.convertor[16] = self.to_hexadecimal

    def to_binary(self, n):
        return int_to_bin(n)

    def to_octal(self, n):
        return oct(n)


