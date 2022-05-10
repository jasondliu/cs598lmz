from _struct import Struct
s = Struct.__new__(Struct)
def __init__(self, *args):
    assert len(args) &gt; 0
    self.format = args[0]
    self.size = s.size
s.__init__ = __init__
print s.format
print s.size
</code>
But I am getting the <code>AttributeError</code> as soon as I call <code>s.__init__</code>:
<code>AttributeError: Struct instance has no attribute '_Struct__format'
</code>
How can I fix this?


A:

I don't know enough about <code>_struct</code> to tell you whether or not the underlying C code will use <code>__format</code>, but regardless, it's a bad idea to try to use <code>__format</code>.
When you subclass built-in types (as you're doing here), you rarely need to access attributes that begin with double-underscores.  The reason Python has them is so that subclasses don't end up trying to overwrite something important, or (more often) so that subclasses can freely add attributes without worrying about clashing with a
