from types import FunctionType
a = (x for x in [1])
print(type(a))    # <class 'generator'>
print(type([1])) # <class 'list'>

# generator内部返回 next自身
def foo():
    for x in range(10):
        yield x
g = foo()
print(type(g))
print(type(foo))
# 迭代一次 游标next指向生成器内部的上一个位置 next自身
n = next(g)      # 执行到第11行
print(n)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

# 列表/字典/集合推导式
a = [x for x
