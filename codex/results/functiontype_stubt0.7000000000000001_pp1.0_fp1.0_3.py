from types import FunctionType
a = (x for x in [1])
b = [1]
c = FunctionType(lambda x: x)
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))

# yield 语句返回一个迭代器对象
def g():
    yield 1
    yield 2
    yield 3

print(isinstance(g(), GeneratorType))

# 下面的示例演示了如何实现可迭代对象和迭代器对象
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children
