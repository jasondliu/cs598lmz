from types import FunctionType
a = (x for x in [1])
type(a)

# 用下面的方法可以判断一个变量是否是生成器generator：
isinstance(a, GeneratorType)

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance((x for x in range(10)), Iterator)
isinstance(iter([]), Iterator)
isinstance(iter('abc'), Iterator)

# 总结：
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是
