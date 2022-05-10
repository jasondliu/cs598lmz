from types import FunctionType
a = (x for x in [1])
print a, type(a)

# 这里要注意到生成器和列表生成式的区别
a = (x for x in [1])
b = (x for x in [1])
print a == b, b == a

# 生成器的函数是每次调用一次，比如这个函数生成一个元组，每次调用产生一个元组
def gen_tuples(n):
    for i in range(n):
        yield i, i

a = gen_tuples(3)
print a.next()
print a.next()
print a.next()
print a.next()


# 第二节 实现一个异步搜索结
