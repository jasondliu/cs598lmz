import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
new_callback = FUNTYPE(lambda *args: 0)
</code>
The <code>lambda</code> just returns a constant integer, I could also use a regular function but for the sake of simplicity I'd like to make it anonymous.
You can now use this callback with <code>libcurl</code> as follows:
<code>import ctypes.util
curl = ctypes.CDLL(ctypes.util.find_library('curl'))

custom_header = []

def write_function(buffer, size, nmemb, userdata):
    userdata.append(buffer[:size*nmemb])
    return size * nmemb

write_function_callback = ctypes.CFUNCTYPE(
    ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_void_p)(write_function)
</code>
Now you
