import ctypes
# Test ctypes.CField

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python setup.py build_ext --inplace --compiler=mingw32')
        sys.exit(1)
    import run_tests # Assumes we're in the test/ directory!
    run_tests.run_tests()
