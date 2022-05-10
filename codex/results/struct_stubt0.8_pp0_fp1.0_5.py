from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('')

# New notation
s = Struct()
s.__init__('i')
s = Struct('i')

# Classical notation (to be used in most cases)
s = Struct('i')

# We can use the result of __new__ directly (of course without passing argument)
s.__new__(Struct)

# __call__ is callable too !
s.__call__('i')

# We can still use the classical notation
s('i')
```

The `Struct` class offers a constructor which takes one argument as string, with which we can specify the format of the Struct.

We can create a Struct with:
```python
s = Struct('iiii')
```

This will create a Struct with a format of four `i`. 

We can retrieve the format with `s.format`.

We can now create a buffer, which we'll use to store our struct data.

```python
from _buffer import Buffer
# Create a Buffer
b = Buffer()

# Write tuples of struct data in the buffer.
