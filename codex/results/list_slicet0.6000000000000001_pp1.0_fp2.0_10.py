import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(lst)

# 输出结果：
# 计算完成后，lst为空列表，如果上面的代码中把callback中del lst[0]去掉，则lst将变为['']
# 可以看出，callback被执行了，而且callback中的lst指向的是原来的lst列表

# 总结：
# 对象的弱引用计数为0时，被回调函数调用
# 回调函数中的参数是可选的，如果没有，则回
