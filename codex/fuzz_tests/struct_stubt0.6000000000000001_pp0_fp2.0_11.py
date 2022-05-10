from _struct import Struct
s = Struct.__new__(Struct)
s.size = s.sizeof(Struct)
</code>
But I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: _struct.Struct.__new__(Struct): not enough arguments
</code>
I am trying to find the size of the structure object that is used by the struct module, so that I can create my own object with the same size.
Edit:
I am not interested in the size of the struct object itself, I am interested in the size of the struct object that is created when you call <code>Struct.__new__(Struct, format)</code>


A:

<code>Struct</code> is not a class, it's a factory function. It returns a class, but you can't use <code>__new__</code> on it.
You could use:
<code>Struct.__new__(Struct, "B").size
</code>
or
<code>Struct("B").size
</code>

