import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def callback(func):
    def wrapper(*args, **kwargs):
        return FUNTYPE(func)(*args, **kwargs)
    return wrapper

@callback
def test():
    print("Hello World")

test()
</code>

