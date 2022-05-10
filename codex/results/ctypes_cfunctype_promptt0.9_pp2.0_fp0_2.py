import ctypes
# Test ctypes.CFUNCTYPE for function pointers
# which require parameters
make_pointer = ctypes.CFUNCTYPE(
    ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)
# Prepare C interface
c_serial_io = ctypes.CDLL(
    os.path.join(os.path.dirname(__file__), 'serial_io_c.dll'))
c_serial_io.init_serial.argtypes=(ctypes.c_char_p,
                                  ctypes.c_char_p,
                                  ctypes.c_char_p,
                                  ctypes.c_int)
c_serial_io.start_read.argtypes = (ctypes.c_void_p,
                                   ctypes.c_bool,
                                   ctypes.c_void_p,
                                   make_pointer)
# Line input function
def line_input_c(ptr, l):
    # On Windows the serial input is captured in a separate thread
    # when the serial is initiated. The read buffer is continually
   
