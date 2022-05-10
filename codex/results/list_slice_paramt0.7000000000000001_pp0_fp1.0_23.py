import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
</code>
I am trying to understand the following code. After a is deleted,the callback is called,this part I understand,but what does the following statement mean?
<code>del lst[0]
</code>
How is the callback function related to <code>del lst[0]</code>?


A:

If you try to run the code, it will give you the following:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: 'str' object doesn't support item deletion
</code>
The callback tries to remove the first item from the list, but <code>str</code> objects cannot be modified (i.e. you can't delete items from them). This code is not a valid example.

