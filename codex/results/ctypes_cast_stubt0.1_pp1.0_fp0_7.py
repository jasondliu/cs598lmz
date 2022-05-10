import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes模块调用C函数
# 定义一个C函数
# int add(int a, int b)
# {
#     return a + b;
# }
# 定义一个C函数指针
# typedef int (*p_add)(int, int);
# 定义一个C函数指针数组
# typedef p_add (*p_add_array)[10];
# 定义一个C函数指针数组指针
# typedef p_add_array (*p_add_array_pointer)[10];
# 定义一个C函数指针数组指针指针
# typedef p_add_array_pointer (*p
