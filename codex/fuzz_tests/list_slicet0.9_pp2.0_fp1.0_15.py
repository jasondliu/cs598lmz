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
print "no output is expected"
</code>
Expected is to get no error/output, but instead the program freezes. Any ideas? 
EDIT again:
I forgot to add that the problem disappears when I remove the <code>while</code>-statement and just let the program terminate. More bizarre (to me, at least) is that even when the program segfaults, the <code>del lst[0]</code>-statement doesn't show if I execute/disasemble the code with gdb/objdump. 
EDIT again:
Okay, found the cause for the segfault. I forgot to post the value for <code>CYTHON_TRACE</code>, which is given by the Makefile and shows the variable value where it is used. In the Makefile you will find the line <code>CYTHON_TRACE=1</code>. When executing the Python version of the code, it seems to have no influence, but when I execute the C-version, there is a segfault.


A:

Ah, you didn't give us your <code>track()</code>
