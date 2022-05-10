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
print lst

#lst=['a','b',['c','d']]
# a = []
# a.append(lst)
# print a
# a.append(lst[2])
# print a
# print a[0]
# print a[1]
# print a
# a[0][0] ='e'
# print a[0]
# print a[1]
# print a

# # 可变长参数
# def test(name, *params):
#     print name, params
#
#
# test('duan', 'age', 'sex', 'job')
#
# # 关键字参数
# def test_kwarg(name, **params):
#     print name, params
#
#
# test_kwarg('duan', age=27, sex='male', job='hacker')
#
# # 命名关键字参数
# def test_namedkwarg(name, *, age,
