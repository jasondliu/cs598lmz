import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def store(d):
    d.x = 1
    d.y = 2
    d.z = 3
    return d

def load(d):
    return d.x, d.y, d.z

def main():
    d = S()
    store(d)
    print(load(d))

main()
</code>

