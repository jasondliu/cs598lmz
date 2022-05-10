from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 从上面的输出可以看出，__code__属性的第一个元素是函数的参数个数。
# 第二个元素是函数的局部变量个数。第三个元素是函数的字节码对象。
# 第四个元素是一个元组，包含了函数的所有常量。
# 第五个元素是函数的名字。第六个元素是函数的文件名。
# 第七个元素是函数的
