import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a ;b=A();b.c=a
keepali0e.append(a)
keepali0e.append(b)
weakref.ref(b,callback)
weakref.ref(b.c,callback)
del a ; del b
if __name__=="__main__":
    import gc;gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
    gc.collect();print lst,len(gc.garbage)
    while not gc.garbage:
        import gc;gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
        gc.collect();print lst,len(gc.garbage)
</code>
So it does what I want it to do when I comment out the gc test loop.  When I have the test loop, it keeps printing an empty list and len() of 0, and it never ends.
Can anyone tell me why this is happening?  If you have a better solution to my problem, I'd be glad to hear it.
Update:  OK, so I discovered the answer for this specific case.  The fact that
