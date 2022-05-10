fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: 'generator' object is not callable

# 使用类的方法
class A:
    def __call__(self, *args, **kwargs):
        print('__call__')

a = A()
a()

# __call__

# 使用类的方法
class A:
    def __call__(self, *args, **kwargs):
        print('__call__')

a = A()
a()

# __call__

# 使用类的方法
class A:
    def __call__(self, *args, **kwargs):
        print('__call__')

a = A()
a()

# __call__

# 使用类的方法
class A:
    def __call__(self, *args, **kwargs):
        print('__call__')

a = A()
a()

# __call__

# 使用
