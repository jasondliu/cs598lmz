import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def say_hello(a, b):
    print(a, b)
    return 42

a = FUNTYPE(say_hello)
print(a(1, 2))
print(a(3, 4))

# 输出结果
# 1 2
# 42
# 3 4
# 42
```


##pybind11

```
// test.cpp
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function which adds two numbers");
}
```

```
# setup.py
from setuptools import setup
from set
