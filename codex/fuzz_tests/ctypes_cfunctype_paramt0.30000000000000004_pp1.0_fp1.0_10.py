import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def get_fun(lib, name):
    return FUNTYPE(lib.get_function(name))

def get_fun_from_lib(lib, name):
    return FUNTYPE(lib[name])

def get_fun_from_lib_by_index(lib, index):
    return FUNTYPE(lib[index])

def get_fun_from_lib_by_name(lib, name):
    return FUNTYPE(lib[name])

def get_fun_from_lib_by_ordinal(lib, ordinal):
    return FUNTYPE(lib[ordinal])

def get_fun_from_lib_by_ordinal_and_name(lib, ordinal, name):
    return FUNTYPE(lib[ordinal])

def get_fun_from_lib_by_ordinal_and_name_and_flags(lib, ordinal, name, flags):
    return FUNTYPE(lib[ordinal])

def get_fun_from_lib_by
