from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)
</code>
But I'm not sure if that's the right way to go about it.
Is there a way to do this without copying the source code?


A:

You can use <code>__new__</code> to create an instance of the <code>Struct</code> class, but you can't use it to initialize the instance.  The <code>__new__</code> method is called before the <code>__init__</code> method, and it is supposed to return a new instance of the class.  If you want to use <code>__new__</code> to initialize the instance, then you have to return an already initialized instance.  For example:
<code>&gt;&gt;&gt; class MyStruct(Struct):
...     def __new__(cls, format):
...         return Struct.__new__(cls, format)
...     def __init__(self, format):
...         print('__init__ called')
...
&gt;&gt;&gt; s = MyStruct('
