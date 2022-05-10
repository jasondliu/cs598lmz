from _struct import Struct
s = Struct.__new__(Struct).__init__('=f')
print(s)
#struct.Struct('=f')
#The above doesn't work for me.
</code>
My question is: How can I call the Struct constructor without passing in a format string? If it is not possible to call the constructor without passing a format string, is it possible to create a Struct object without passing a format string?


A:

Actually, struct.Struct is a regular class, it's <code>__init__</code> method is documented in the docs, so it's possible to call it without arguments, of course, it won't create a complete object if you don't provide all the arguments the method is expecting.
<code>&gt;&gt;&gt; help(struct.Struct.__init__)
Init signature: struct.Struct.__init__(*args, **kwargs)
</code>
From the constructor,
<code>def __init__(self, format):
    """Returns a new Struct object which writes and reads binary data according
    to the format string.
</code>
and
<code>TypeError: Required argument 'format' (pos
