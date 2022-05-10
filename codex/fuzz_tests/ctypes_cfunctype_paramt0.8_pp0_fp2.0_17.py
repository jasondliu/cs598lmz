import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double)

c_draw_func = FUNTYPE(draw_func)

so = ctypes.CDLL('./libdraw.so')
so_draw_boundbox = so.draw_boundbox
so_draw_boundbox.restype = None
so_draw_boundbox.argtypes = [ctypes.c_double, ctypes.c_double,
                            ctypes.c_double, ctypes.c_double,
                            ctypes.c_double, ctypes.c_double,
                            ctypes.c_double, ctypes.c_double,
                            ctypes.c_double, ctypes.c_double,
                            ctypes.c_double, ctypes.c_double,
                            FUNTYPE]

so_draw_solid_rect = so.draw_solid_rect
so_draw_solid_rect.argtypes =
