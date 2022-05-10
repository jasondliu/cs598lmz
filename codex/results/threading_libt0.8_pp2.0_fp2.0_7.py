import threading
threading.Thread(target=foo,args=(1,)).start()
</code>
It seems that this approach is not sufficient.
How can I make a temporary alias for a given function or object while the alias still exists?


A:

You can create a new function with the desired name, and then assign it to the original function.
<code>def foo_real(x):
   return x+1

def foo(x):
    return x+2

globals()["foo"] = foo_real

print(foo(4))
# 5
</code>

