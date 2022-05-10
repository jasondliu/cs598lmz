import ctypes
ctypes.cast(id(42), ctypes.py_object).value
```

```
42
```
## 49. Does Python support function overloading?

Yes. Using factory functions and closures, we can implement function overloading in Python.

## 50. What is the difference between list and tuple?

- A tuple is immutable while a list is mutable.
- A list has various functions that help to modify it but a tuple has very limited built-in functions.
- A tuple is generally used for heterogeneous (different) datatypes and a list is used for homogeneous (similar) datatypes.
- A tuple is hashable while a list is not. Tuples can be used as a key for a dictionary. Lists can not be used as keys for dictionaries.
## 51. What is the difference between deep and shallow copy?

Shallow copy is used when a new instance type gets created and it keeps the values that are copied in the new instance. Shallow copy is used to copy the reference pointers just like it copies the values. These references point to the original objects and the changes made in any member of the class will also affect the original copy of it
