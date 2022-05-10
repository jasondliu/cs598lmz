import ctypes
# Test ctypes.CFUNCTYPE()

# kqueue
kevent_type = ctypes.CFUNCTYPE(ctypes.c_int,
                               ctypes.POINTER(kevent),
                               ctypes.POINTER(kevent),
                               ctypes.c_int)
test_func = kevent_type(None)
test_func # doctest: +ELLIPSIS

# dlopen
dlerror_type = ctypes.CFUNCTYPE(ctypes.c_char_p)
test_func = dlerror_type(None)
test_func # doctest: +ELLIPSIS

# epoll
epoll_type = ctypes.CFUNCTYPE(ctypes.c_int,
                              ctypes.c_int,
                              ctypes.POINTER(epoll_event))
test_func = epoll_type(None)
test_func # doctest: +ELLIPSIS

# solaris
port_notify_function_type = ctypes.CFUNCTYPE(ctypes.c_int,
                                             ctypes.
