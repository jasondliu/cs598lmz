import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

def lua_newstate():
    lua_newstate = lib.lua_newstate
    lua_newstate.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    lua_newstate.restype = ctypes.POINTER(lua_State)
    return lua_newstate(lib.lua_alloc, None)

def lua_close(L):
    lib.lua_close(L)

def lua_open():
    return lua_newstate()

def lua_newthread(L):
    return lib.lua_newthread(L)

def lua_atpanic(L, panicf):
    lib.lua_atpanic.argtypes = [ctypes.POINTER(lua_State), FUNTYPE]
    lib.lua_atpanic.restype = FUNTYPE
    return lib.lua_atpanic(L, panicf)

def lua_gettop(L):
    lib.lua_gettop.argtypes = [ctypes.PO
