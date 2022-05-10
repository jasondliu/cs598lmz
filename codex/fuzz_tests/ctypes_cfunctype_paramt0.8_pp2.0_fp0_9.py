import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)
def make_callback(val):
    return FUNTYPE(lambda i: val)

>>> f = ctypes.cdll.msvcrt.malloc
>>> f(10)
4855200
>>> f.restype = ctypes.c_int
>>> f.argtypes = FUNTYPE,
>>> f(make_callback(42))
42
>>> f(make_callback(300))
300
>>> f(42)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be convertible to a pointer
```

```c
#include <stdlib.h>

typedef int (*callback)(int);

void *f(callback f)
{
    return malloc(f(3));
}
```


## More examples

```c
#include <stdio.h>

int main(int argc, char **argv)
{
    if (argc == 2)
        printf(argv[1
