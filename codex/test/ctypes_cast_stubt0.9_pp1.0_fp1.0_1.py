import ctypes
ctypes.cast(int("4242", 16), ctypes.c_void_p).value

def trap_error():
    try:
        raise KeyError("Bad key error")
    except KeyError as ke:
        print("Key error: " + ke)


