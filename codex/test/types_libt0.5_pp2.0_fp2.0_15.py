import types
types.FunctionType

def fn():
    pass

type(fn)

type(abs)

# isinstance()
# 能用type()判断的基本类型也可以用isinstance()判断
isinstance('a', str)

isinstance(123, int)

isinstance(b'a', bytes)

# 判断一个变量是否是某些类型中的一种
isinstance([1, 2, 3], (list, tuple))

isinstance((1, 2, 3), (list, tuple))

# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数
dir('ABC')

len('ABC')
'ABC'.__len__()

# 配合get
