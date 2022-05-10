import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def call_func(func, arg):
    func(arg)

def callback(arg):
    print 'callback', arg
    return 0

def main():
    func = FUNTYPE(callback)
    call_func(func, 1)

if __name__ == '__main__':
    main()
</code>
The output of this code is:
<code>callback 1
</code>

