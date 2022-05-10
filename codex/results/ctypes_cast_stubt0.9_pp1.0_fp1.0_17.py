import ctypes
ctypes.cast(0, type=None)
<built-in method cast of _ctypes.PyCArgObject object at 0x0000000002DFBF50>
```

这个方法的定义在[dll.h](https://github.com/python/cpython/blob/master/Modules/_ctypes/dll.h#L28)中，知道了方法中定义要从哪个头文件中寻找，就比较好定位了，比较1000多行代码定位到[第九十七行](https://github.com/python/cpython/blob/master/Modules/_ctypes/callproc.c#L97)：

```c
static void
_build_arglist(ffi_cif *cif,
               CallArgs *args,
               ffi_type **argtypes,
