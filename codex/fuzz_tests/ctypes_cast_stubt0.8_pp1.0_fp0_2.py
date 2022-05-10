import ctypes
ctypes.cast(0x12345678, ctypes.c_void_p).value

# Expected output
419712824
```

Another solution could be to use `id` function to get memory address of an object.
And then using `hex` function to get hexadecimal format of this memory address.

```python
# Python
id(value)

# Expected output
127513728

hex(id(value))

# Expected output
'0xa8003c0'
```

### Recursion

* [Recursion](https://en.wikipedia.org/wiki/Recursion) is a way of thinking about and solving a problem.
* [Recursion](https://en.wikipedia.org/wiki/Recursion) is when a function calls itself, either directly or indirectly.
* The recursive function must have a [base case](https://en.wikipedia.org/wiki/Base_case) to avoid infinite calls.
* To prevent infinite recursion, use a counter or some other mechanism to track the number of times a particular function has been called.
* In Python, there's a [
