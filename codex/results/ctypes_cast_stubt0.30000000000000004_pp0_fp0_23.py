import ctypes
ctypes.cast(1, ctypes.py_object)

# 一个更实用的例子，利用ctypes实现对C语言动态库的调用
# 使用ctypes来调用C语言动态库
# 下面是一个简单的C语言动态库，它定义了一个函数add，两个整数相加
# 将以下代码保存为add.c
'''
int add(int a, int b) {
    return a + b;
}
'''
# 使用gcc编译成动态库
# gcc -shared -o libadd.so -fPIC add.c

# 用ctypes调用该
