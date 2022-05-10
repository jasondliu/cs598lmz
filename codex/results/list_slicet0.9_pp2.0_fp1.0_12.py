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
</code>
Procedure for the above program
<code>def main():
    a = A()
    a.c = a  # create a cyclic reference
    keepalive.append(weakref.ref(a, callback))  # make a WeakSet of all live references to a, and set callback() to be called when a is dead
    del a
    while list:
        keepalive.append(list[:])
    return 0
</code>
Python documentation on WeakSet
https://docs.python.org/3.3/library/weakref.html
What I understand is
1) A function is passed through the WeakSet class for reference checking
2) It checks whether a is alive or not
3) If not it deletes the weak reference
4) Now in my program a is used again in the while loop so how can it be deleted by the callback function
https://repl.it/repls/LiterateReasonableFtp


A:

<blockquote>
<p>4) Now in my program a is used again in the while loop so how can it be deleted by the callback function
