import ctypes
ctypes.cast(100000, ctypes.py_object)()

#"""

def testdll():
    import ctypes
    dllabspath = r"D:\Code\Python\test.dll"
    dll = ctypes.CDLL(dllabspath)
    print(dll)

def main():
    # testdll()
    test()
    # testpackage()


if __name__ == '__main__':
    main()
