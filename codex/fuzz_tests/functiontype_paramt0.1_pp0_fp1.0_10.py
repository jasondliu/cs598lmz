from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
# CodeType(argcount, nlocals, stacksize, flags, codestring, constants, names, varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])
# argcount: 整数，参数个数（不包括 *args 和 **kwargs）
# nlocals: 整数，局部变量个数
# stacksize: 整数，堆栈深度
# flags: 整数，标志位
# codestring: 字节串，字节码
# constants: 元组，常量
# names: 元组，函数内部引用的全局名字

