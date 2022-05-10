from _struct import Struct
s = Struct.__new__(Struct)
print s
</code>
If you want to make a custom class that will accept an argument when you instantiate an instance, that needs to be implemented in <code>__new__</code>:
<code>class MyClass(object):
    def __new__(cls, arg):
        # this is where you would do some magic with arg
        return object.__new__(cls)
</code>
Instead of either of these two options, you can just create instances of <code>struct.Struct</code> like so:
<code>s = Struct(arg)
</code>
You don't really need to subclass <code>struct.Struct</code> at all. But if you do want to subclass it, you'll just want to override <code>__new__</code>; specifically, you want to call the <code>struct.Struct.__new__()</code> method and pass it in <code>arg</code> as the first parameter:
<code>class MyClass(Struct):
    def __new__(cls, arg):
        # arg must be a string
        return super(MyClass
