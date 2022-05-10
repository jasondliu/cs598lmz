import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 7
assert fun() == 7
```

```python
# ctypes can also wrap dylibs, similar to cffi
luamod = ctypes.CDLL(os.path.join(LUA_MOD_DIR, 'luawrap.so'))
assert luamod.pywrap_init(0) == None
res = luamod.pywrap_run(b'7')
assert res.value == 7
```

```python
# luajit has a C api for integrating with Python and other languages
luajit = ctypes.CDLL(os.path.join(LUA_MOD_DIR, 'libluajit-5.1.so.2'))
# initialize
L = jit.luaL_newstate()
assert L != None
# do stuff, load libs...
luajit.luaL_openlibs(L)
# load a string into the stack
res = jit.luaL_loadstring(L, b'return ctypes.cast(0, ctypes.POINTER(ctypes.c_uby
