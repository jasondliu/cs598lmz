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
keepali0e=None</pre></td></tr>
</table>



</center>

---

### Keepalives:
This is a simple example of how to use keepalives. It will be used through out the rest of this article as a simple example of a system that uses keepalives

### What is a keepalive?
A keepalive is a special kind of weakref that you can use to keep objects alive for a certain period of time. It's best use is to keep objects alive for the time of some callback function.

### Why use keepalives?
For long there have been problems with keeping objects alive for the time of a callback function. This means that if you have a callback from some other module, and you want to pass a python object as an argument to that callback, you would have to make sure that object stays alive for the whole time of the callback call.

### How does it work?
It is pretty simple really. It stores a weakref to the object and it's callback function. When the GC removes the object, the callback is called.

### What are keepalives used for?
The best
