import ctypes
ctypes.cast(0, ctypes.py_object)

# 使用ctypes模块调用C函数
# 定义一个C函数
# int add(int a, int b)
# {
#     return a + b;
# }
#
# # 定义一个C函数指针
# int (*p)(int, int);
#
# # 将C函数赋值给C函数指针
# p = add;
#
# # 调用C函数
# int c = p(3, 4);
#
# # 输出结果
# printf("c = %d\n", c);
#
# return 0;

# 定义一个C函数
# int add(int a, int b)
# {
#     return a + b;
# }
#
# //
