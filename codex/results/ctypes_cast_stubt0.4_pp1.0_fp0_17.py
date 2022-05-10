import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes模块

# 使用ctypes模块可以调用C语言库函数
# 下面是一个使用ctypes模块调用C语言库函数的示例
# 定义一个C语言库函数
# 定义C语言库函数的头文件
"""
#include <stdio.h>
void hello(char *s) {
    printf("Hello, %s\n", s);
}
"""
# 使用ctypes模块调用C语言库函数
# 导入ctypes模块
import ctypes
# 加载动态
