import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes调用C函数
# 定义一个C函数
# int add(int a, int b) {
#     return a + b;
# }
# 将C函数编译成动态链接库
# gcc -shared -o libadd.so -fPIC add.c
# 在Python中调用
# import ctypes
# lib = ctypes.cdll.LoadLibrary('./libadd.so')
# print(lib.add(1, 2))
# 3

# 使用ctypes调用C++函数
# 定义一个C++函数
# int add(int a, int b) {
#     return a + b;
# }
# 将C++函数编译成动态链接库
