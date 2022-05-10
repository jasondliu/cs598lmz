import io
class File(io.RawIOBase):
  ...
</code>
I need to subclass <code>File</code> here.
I can do it with the <code>__metaclass__</code> attribute. 
<code>class File(io.RawIOBase):
  __metaclass__ = MyMetaClass
</code>
But it looks like a dirty hack. I prefer a more pythonic way. 
Later Update As @aeidreos has told this question is solved in the python official documentatation of data model.


A:

You can just specify the metaclass of the <code>MyClass</code> in the class declaration. You can do it in several ways:
<code>class MyClass(metaclass=MyMetaClass):
    pass

class MyClass(object):
    __metaclass__ = MyMetaClass
</code>
If you need to subclass <code>File</code>, you should pass the <code>metaclass</code> as an argument:
<code>class File(io.RawIOBase, metaclass=MyMetaClass):
    pass
</code>

