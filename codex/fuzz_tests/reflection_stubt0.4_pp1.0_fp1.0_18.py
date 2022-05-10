fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# 下面代码会抛出TypeError异常，因为没有定义__call__方法
class C:
    def __init__(self, x=0):
        self.x = x
c = C()
c()

# 下面代码会抛出TypeError异常，因为__call__方法的参数不对
class C:
    def __call__(self, a, b):
        return a + b
c = C()
c(2)

# 下面代码会抛出TypeError异常，因为__call__方法的参数不对
class C:
    def __call__(self, a, b, c):
        return a + b
c = C()
c(2, 3)

# 下
