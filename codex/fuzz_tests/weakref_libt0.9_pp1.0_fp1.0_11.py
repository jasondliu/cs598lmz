import weakref

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair(%r, %r)' % (self.x, self.y)
    def __str__(self):
        return 'Pair(%r, %r)' % (self.x, self.y)

def callback(reference):
    print('callback'), reference, 'has been called'

a = Pair(2,3)
b = Pair(4, 5)
b.x = a.x
a_w = weakref.proxy(a, callback)
# a = 'abc' # 注释，a成为垃圾，且回调被触发，否则不调用回调
b.x = 'abc'
print(a_w.x)
print(b.x)
