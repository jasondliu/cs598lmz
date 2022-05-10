import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
del a,keepali0e
print('end')
</code>
Output:
<code>123
&lt;ref at 0x0000000001A6CD70; dead&gt;
&lt;ref at 0x0000000001A7D1C0; to 'None' at 0x00000000022B5710&gt;
end
</code>


A:

To avoid this, use only one reference to the object anywhere. 
What's happening here is that the <code>keepalive[0]</code> is holding a reference open. 
Once you do <code>del a,keepalive[0]</code> the callback gets triggered and <code>lst[0]</code> is removed. 

