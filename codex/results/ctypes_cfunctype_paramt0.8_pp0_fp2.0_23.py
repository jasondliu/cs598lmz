import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)
COUNT = FUNTYPE(count)
try:
    libc = ctypes.CDLL("libc.so.6")
except OSError:
    # In case the above failed, try loading the same library
    # from platform-specific place.
    try:
        libc = ctypes.CDLL("libc.so")
    except OSError:
        # Failed again.
        print("Failed to load libc.so")

# Set COUNT to be the signal handler
libc.signal(signal.SIGINT, COUNT)

def main():
    while True:
        time.sleep(1)
        print("Interval!")

if __name__ == "__main__":
    main()
</code>
Now, when I run it, I get an <code>Illegal instruction</code> error.
<code>$ python3 siginterrupt.py
Interval!
Interval!
Interval!
Illegal instruction

