import weakref

class A(object):
    pass

a = A()
d = weakref.WeakValueDictionary()
d['primary'] = a
print('d["primary"]= ', d['primary'])
del a
print('d["primary"]= ', d['primary'])
</code>
Output:
<code>d["primary"]=  &lt;__main__.A object at 0x7fd2d1e24c10&gt;
d["primary"]=  None
</code>

