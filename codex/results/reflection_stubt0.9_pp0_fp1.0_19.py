fn = lambda: None
gi = (i for i in ())
fn.__code__ = type(gi.gi_code)
fn.__code__.co_lnotab = "┘┘┴┴┴"
fn()
```

The string `"┘┘┴┴┴"` is an overlong UTF-8 string. This causes iteration over the lnotab to cause an exception, and since `next_instr` is not called, the execution continues from an uninitialized instruction pointer. This can be used to cause an access violation, which results in SIGSEGV.

Predicting the address of the instruction pointer is fairly easy. Since there are four instructions in the loop, the address of the code object plus a constant is sufficient to get the code object's address, as well as the instruction pointer just before the instruction pointer is initialized, as follows:
```python
a[0] = fn.__code__.co_code[:5] + struct.pack("<Q", fn.__code__ + 216)
```

Note that the endianness must be considered. Also note that the constant 216 was found by trial and error.

Now, to actually make the access violation
