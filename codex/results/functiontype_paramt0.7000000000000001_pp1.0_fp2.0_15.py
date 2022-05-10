from types import FunctionType
list(FunctionType(my_code, globals(), 'my_func'))

# Returns: [<function my_func at 0x7f0d5e5a5268>, <function my_func at 0x7f0d5e5a59d8>]

```


```python
a = list(FunctionType(my_code, globals(), 'my_func'))

# Returns: <function my_func at 0x7f0d5e5a5268>

```


```python

# Returns: <function my_func at 0x7f0d5e5a59d8>

```


```python
def add(a, b):
    return a + b

# Returns:
add.__code__.co_code
# b'|\x00|\x01\x17\x00S\x00'

# b'|\x00|\x01\x17\x00S\x00'

# b'|\x00|\x01\x17\x00S\x00'
