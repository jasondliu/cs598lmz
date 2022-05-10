import ctypes
ctypes.cast(self.__data, ctypes.POINTER(T))[index]
</code>
(I wonder if there were some other smarter way to do this in Cython, as well)
My question here is: could I have cast to the ctype from somewhere other than the ndarray (or some other buffer) directly?  I've read about <code>pointer(..., type=T)</code>, but I'd rather not introduce another pointer.
Or am I just better off overloading <code>__getitem__()</code> for the class so anybody else can use it just like an ndarray (or some other buffer...)?  (If I do overload <code>__getitem__()</code>, I think I can use the numpy type system to guarantee that the class represents contiguous data.)

Edit: Adding a couple more possibilities.
Option 1
Here's another way to get the expected pointer.
<code>cdef size_t index = i
p = &lt;T *&gt;(&amp;self.__data[0] + index)
result = p[0]
$&gt;&gt;r epr(
