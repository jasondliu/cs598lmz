import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
print lst
</code>
I would except that <code>A</code>'s instance's <code>c</code> attribute to be <code>None</code> or <code>callback</code> function to make <code>lst</code> list have 2 elements,instead it behaives as:
<code>python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 00:54:21) [MSC v.1600 32 bit (In
tel)] on win32
Type "copyright", "credits" or "license()" for more information.
&gt;&gt;&gt; ================================ RESTART ================================
&gt;&gt;&gt; 
Traceback (most recent call last):
  File "D:\My Codes\Weakef.py", line 10, in &lt;module&gt;
    del a
  File "D:\My Codes\Weakef.py", line 8, in callback
    del lst[0]
NameError: name '
