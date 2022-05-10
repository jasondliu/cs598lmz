import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print fun() # => 42
```

## General syntax

### Function types

Function types are declared with the `fun` keyword and have the general form:

```
fun (
  (type | auto) identifier,
  (type | auto) identifier,
  ...
  (auto ... | type ...)
) -> return_type;
```

The last argument can be a variadic arguments list and/or a variadic return
type.

Example:

```
fun (int a, auto ...) -> ret_type ... {}
```

### Argument types

Arguments can be of 3 kinds:

- **simple**: the argument is just an integer, a string, an array, ...
- **dereference**: the argument is a pointer to an integer, a string, an array, ...
- **reference**: the argument is an integer, a string, an array, ... that can
  be modified by the function.

The type of the arguments is declared using brackets: `[type]` for
dereferences, `&type` for
