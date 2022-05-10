from _struct import Struct
s = Struct.__new__(Struct)
from array import array
a = array.__new__(array)
</code>
What's the difference? In both cases I just created objects, but one I created from the factory function and one from the class. If a class is a factory function, then why do I need to use factory function?


A:

"What's the difference?"
In your first case you are calling the <code>__new__</code> method of a class (your example is <code>Struct</code>) with the arguments passed to the <code>open</code> function, while in the second case you are calling the <code>__new__</code> method of your <code>File</code> class with the arguments passed to the <code>File</code> class itself.
"If a class is a factory function, then why do I need to use factory function?"
Here you are mixing two different concepts. A class is not a factory function. I guess you mean that the <code>__new__</code> method can be used to make an instance of that class. But that has nothing to do with a factory function.
"Why are objects created from the factory
