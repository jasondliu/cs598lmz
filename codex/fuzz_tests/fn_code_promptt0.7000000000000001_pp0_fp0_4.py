fn = lambda: None
# Test fn.__code__
expect(fn.__code__, {
    "co_argcount": 0,
    "co_cellvars": (),
    "co_code": b"d\x00\x00S",
    "co_consts": ("None",),
    "co_filename": "<ipython-input-4-9f73fdb1d121>",
    "co_firstlineno": 1,
    "co_flags": 67,
    "co_freevars": (),
    "co_kwonlyargcount": 0,
    "co_lnotab": b"\x00\x01\x0c\x01",
    "co_name": "fn",
    "co_names": ("None",),
    "co_nlocals": 0,
    "co_stacksize": 2,
    "co_varnames": ()
})

# Test fn.__globals__
expect(fn.__globals__, {
    "__name__": "__main__",
    "__doc__": None,
   
