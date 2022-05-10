import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(1)
    _fields_ = [("x", ctypes.c_long)]

def f(*args):
    pass

def f2(*args):
    pass

def call(f, args):
    f(args)

def main():
    s = S()
    call(f, s)
    call(f2, s)

main()
