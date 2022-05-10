import weakref
# Test weakref.ref on functions.
#把一个函数转化成弱引用形式
#将一个c函数转化为弱引用形式
c=2
def f():
    global c
    print c
    c+=1
#以下表达式返回f函数的弱引用，即内存清理时会自动将其释放
fw=weakref.ref(f)
f()
1
#此时回调对象有效
fw()
1
f=3
#此时回调对象无效
fw()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ReferenceError: weakly-referenced object no longer exists
