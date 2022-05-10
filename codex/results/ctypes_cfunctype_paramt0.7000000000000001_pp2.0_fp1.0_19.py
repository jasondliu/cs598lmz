import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_char_p)

def set_callback(callback, suffix=''):
    cb = FUNTYPE(callback)
    if len(suffix) == 0:
        lib.set_callback(cb)
    else:
        lib.set_callback_suffix.argtypes = [FUNTYPE, ctypes.c_char_p]
        lib.set_callback_suffix(cb, suffix)


def get_count():
    return lib.get_count()


def get_name(idx):
    return lib.get_name(idx)


if __name__ == '__main__':
    set_callback(lambda x: print(f'callback: {x}'))
    print(f'count: {get_count()}')
    set_callback(lambda x: print(f'callback2: {x}'), 'second')
    print(f'count: {get_count()}')
