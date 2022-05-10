import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def register_callback(callback):
    """
    Register a callback function.
    """
    global _callback
    _callback = FUNTYPE(callback)
    _lib.register_callback(_callback)

def run_callback(arg):
    """
    Run the callback.
    """
    _lib.run_callback(arg)

def main():
    """
    Main function.
    """
    register_callback(lambda x: x*x)
    print(run_callback(10))

if __name__ == '__main__':
    main()
</code>
The code above works, but I am concerned with the <code>global _callback</code> line.  Is there a better way to do this?  I am not sure if this is a good way to do this.


A:

I think you can just use <code>ctypes.CFUNCTYPE</code> directly:
<code>import ctypes

def register_callback(callback):
    """
    Register a callback function.
