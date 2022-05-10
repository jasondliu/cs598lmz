fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
print(fn())


def gen():
    yield 1


g = gen()
print(g)
print(g.__next__())
print(gen())
print(gen().__next__())
# g.__next__()
# -----------------------------------------------------------------------
# 生成器的函数调用


def f():
    x, y = 1, 2
    pr = (yield x, y)
    print('pr: %s' % pr)
    yield x, y
# 对于生成器，也可以使用send()、throw()进行调用
g = f()
print(g.send(None))
print(g.send('Hello!'))
try:
    print(g.throw(RuntimeError, 'Error'))
except RuntimeError as err:
    print('err:', err)
# -----------------------------------------------------------------------
# 生成器的其他属性
def gen():
    yield 1

