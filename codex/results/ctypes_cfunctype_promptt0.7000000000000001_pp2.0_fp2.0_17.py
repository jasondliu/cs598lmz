import ctypes
# Test ctypes.CFUNCTYPE

# Declare callback function
# This is the signature that must match the callback function
CB_FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Declare a variable for the callback function
cb_func = CB_FUNC()

# Declare a variable for the library handle
mylib = ctypes.CDLL('target/debug/libcallback.so')

# Add the callback function to the variable
# This should return the address of the callback function
cb_func.value = mylib.add(5, 7)

# Call the callback function
print(cb_func(5, 7))
```

```
$ python3 ctypes_using_lib.py
12
```

## Rust

``` rust
#[no_mangle]
pub extern "C" fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

```
$ rustc src/main.rs
```

``
