from _struct import Struct
s = Struct.__new__(Struct)
print(s)
</code>
The output is:
<code>&lt;callable-iterator object at 0x7f32e00e9b70&gt;
</code>
I don't understand what this means. To me, it seems like <code>Struct</code> has no <code>__new__</code> method. Calling <code>Struct.__new__</code> gets you a different object than when creating a new <code>Struct</code> object by calling <code>Struct</code>. 

Can someone explain what happened in the output above?
If I want to create an object using <code>Struct.__new__</code>, how do I do so? For example, if <code>X</code> is a class with <code>__new__</code> method, how would I go about calling <code>X.__new__</code> to create a new object of type <code>X</code>?



A:

<code>Struct.__new__</code> calls the function <code>callable_iterator</code> to create a new <code>call
