from _struct import Struct
s = Struct.__new__(Struct)
isinstance(s, Struct)
True
type(Struct)
&lt;class 'type'&gt;
</code>
<code>__new__</code> is a special method that returns an instance of the class, whereas the constructor <code>__init__</code> is used to initialize the instance after creation.

