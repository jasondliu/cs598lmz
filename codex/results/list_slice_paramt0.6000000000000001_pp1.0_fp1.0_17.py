import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a,callback))
del lst
del a
del keepali0e
'''

#print(code)
code='''
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a,callback))
del lst
del a
del keepali0e
'''

code_ob = compile(code, '<string>', 'exec')
#code_ob = compile(code, '<string>', 'exec')
exec(code_ob)
