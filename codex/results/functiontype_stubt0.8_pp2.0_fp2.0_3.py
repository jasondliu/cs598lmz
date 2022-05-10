from types import FunctionType
a = (x for x in [1])
b = (x for x in [1, 2, 3])
print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance(a, Iterable))
print(isinstance(b, Iterable))

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('123'), Iterator))

# 你可能会问，为什么list、dict、str等数据类型不是Iterator？
# 这是因为Python的Iterator对象表示的是一
