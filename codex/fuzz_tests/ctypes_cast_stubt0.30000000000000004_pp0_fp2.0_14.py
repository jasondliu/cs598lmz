import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
# Main

def main():
    """
    Run all tests.
    """
    import sys
    import doctest

    #from numba import vectorize, guvectorize, jit

    #testmod(vectorize)
    #testmod(guvectorize)
    #testmod(jit)

    # Run module doctests
    results = doctest.testmod()
    if results.failed != 0:
        sys.exit(1)

if __name__ == '__main__':
    main()
