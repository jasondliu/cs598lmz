import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
callme = FUNTYPE(lambda x: x+2)
callme(3)

# напишите интерфейс в python к комнатной температуре

import ctypes

def make_ctypes_wrapper(lib_name, func_name):
    lib = ctypes.cdll.LoadLibrary(lib_name)
    func = lib[func_name]
    func.restype = ctypes.c_int
    func.argtypes = [ctypes.c_char_p]
    def wrapper(room):
        encoded_room = room.encode('utf-8')
        return func(encoded_room)
    return wrapper

get_room_temp = make_ctypes_wrapper('./libctypes_example.so', 'get_room_temp')
get_room_temp('living room')

# что
