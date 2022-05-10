import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def call_function(function):
    function()

def main():
    function = FUNTYPE(lambda: print("Hello world!"))
    call_function(function)

if __name__ == "__main__":
    main()
</code>

