from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 生成器只能迭代一次
a = (x for x in [1, 2, 3])
print(list(a))
print(list(a))

# yield from
def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(None)

# 生成器的return语句
def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(None)

# 生成器的return语句
def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(None)

# 生成器的return语句
def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(
