import ctypes
# Test ctypes.CFUNCTYPE()

def func(x, y):
    print('x =', x)
    print('y =', y)
    return x+y

def func_errcheck(result, func, args):
    if result < 0:
        print('Error:', result)
        raise Exception('Error')
    return result

def main():
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
    f.errcheck = func_errcheck
    print(f(2, 3))
    print(f(2, -3))

if __name__ == '__main__':
    main()
