import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('Hello Python!')
lib.my_call(fun)
```

测试：

```bash
# 生成用于调用的动态库
$ gcc -o libmy.so -shared -fPIC my.c
# 生成 python 载入用的库
$ python setup.py build_ext --inplace
# 调用 c 代码
$ python test.py
Hello!
Hello Python!
```

调用时出现问题：无法将 c 函数指针作为参数传递给 c -> c++ 函数，也就是 my_call 函数。

如下代码：

```c++
#include <iostream>

using namespace std;

void hello(void (*funcPtr)
