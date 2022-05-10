from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
# CodeType(argcount, nlocals, stacksize, flags, codestring, constants, names, varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])
# argcount: 整数，函数的参数个数（不包括 *args 和 **kwargs）
# nlocals: 整数，函数的局部变量个数
# stacksize: 整数，函数的栈深度
# flags: 整数，函数的标志
# codestring: 字符串或字节串，函数的字节码
# constants: 元组，函数的常量
#
