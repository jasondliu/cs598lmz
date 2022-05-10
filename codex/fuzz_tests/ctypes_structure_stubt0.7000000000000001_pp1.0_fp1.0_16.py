import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_double
    z = ctypes.c_char*7

def get_struct():
    # x = S(x=12, y=1.23, z='foo')
    x = S()
    x.x = 12
    x.y = 1.23
    x.z = 'foo'
    return x

def print_struct(s):
    # print 'x=%d y=%.2f z=%c' % (s.x, s.y, s.z[0])
    print 'x=%d y=%.2f z=%s' % (s.x, s.y, s.z)

def main():
    s = get_struct()
    print_struct(s)

if __name__ == '__main__':
    main()
