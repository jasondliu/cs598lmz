from _struct import Struct
s = Struct.__new__(Struct)
s.size = Struct.Size(s)
s.format = Struct.Format(s)
s.pack = Struct.Pack(s)
s.unpack = Struct.Unpack(s)
s.unpack_from = Struct.UnpackFrom(s)
</code>
That just gives me a series of:
<code>//s.size = s.size(s);
RuntimeError: maximum recursion depth exceeded
</code>
I suppose that has to do with the fact that the Python version calls a method <code>size</code> in the <code>Struct</code> class which is defined elsewhere, where as the C# version is calling the <code>size</code> method on the instance <code>s</code>. But I don't know how to fix it and I'm not sure whats supposed to happen. Hopefully I'm being quite clear here.
I'm told to use the same signature and parameters as Python. Any help much appreciated, I've been going round in circles.

