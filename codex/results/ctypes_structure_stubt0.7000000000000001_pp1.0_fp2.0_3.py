import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p

def main(argv):
    if len(argv) < 2:
        print "Usage: %s <PyObject>" % (argv[0])
        return 1

    s = S()
    s.x = ctypes.cast(argv[1], ctypes.c_void_p)

    print s.x
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
