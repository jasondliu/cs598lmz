import ctypes
ctypes.cast(myvariable, ctypes.py_object)
```
### Pointer

```
#include <stdio.h>
/*
* 指针用于给函数传递参数，这样在函数中修改p的值，实际上是修改x的值
* 当需要取variabel地址时，就使用取地址运算符'&',将其值赋给指针。
* 指针变量先指向一个变量，再使用取值操作符'*'可以访问这个变量，
* '*'被称为间
