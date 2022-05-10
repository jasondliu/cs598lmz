import gc, weakref

collection = weakref.WeakValueDictionary()


class Class:
    def __init__(self, name):
        self.name = name
        collection[name] = self

    def __repr__(self):
        return '&lt;Class %s&gt;' % self.name


c1 = Class('c1')
c2 = Class('c2')
c3 = Class('c3')


print(collection)
del c2
gc.collect()
print(collection)
</code>
Output:
<code>{'c1': &lt;Class c1&gt;, 'c2': &lt;Class c2&gt;, 'c3': &lt;Class c3&gt;}
{'c1': &lt;Class c1&gt;, 'c3': &lt;Class c3&gt;}
</code>

