import ctypes
ctypes.cast(id(0), ctypes.py_object).value = 'evilvalue'
</code>
<code>id(0)</code> returns the identity of the Python <code>int</code> object with value 0. <code>ctypes.py_object</code> is a C type that corresponds to a Python object. Casting the pointer to <code>ctypes.py_object</code> and accessing its <code>value</code> attribute allows us to change the value of the integer zero to the string <code>'evilvalue'</code>.
Let's try:
<code>&gt;&gt;&gt; 5 + 0
'evilvalue'
</code>
The Python interpreter doesn't like this and throws a <code>TypeError</code>:
<code>TypeError: unsupported operand type(s) for +: 'int' and 'str'
</code>
The interpreter checks for the type of object that it is working with before calling the appropriate operation. Since the operation is <code>+</code>, the interpreter checks the type of the two arguments and verifies they are both integers.
Since the second argument is a string
