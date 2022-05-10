import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:
    pass
</code>
This code will not terminate.

I tried to find a reference cycle in the python source code, but I didn't find any. So I think it's impossible to create a reference cycle in the python source code.
I tried to find a reference cycle in the python standard library, but I didn't find any. So I think it's impossible to create a reference cycle in the python standard library.
I tried to find a reference cycle in the python builtins, but I didn't find any. So I think it's impossible to create a reference cycle in the python builtins.
I tried to find a reference cycle in the python interpreter, but I didn't find any. So I think it's impossible to create a reference cycle in the python interpreter.

So I think it's impossible to create a reference cycle in the python standard library, builtins, interpreter and source code.
Is my thinking correct?

