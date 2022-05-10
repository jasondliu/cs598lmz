import weakref
# Test weakref.ref on functions.
#把一个函数转化成弱引用形式
#将一个c函数转化为弱引用形式
c=2
def f():
    global c
