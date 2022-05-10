fn = lambda: None
# Test fn.__code__
print(fn.__code__)
# <code object <lambda> at 0x107c6da10, file "<stdin>", line 1>

# Test the function
fn()
# UnboundLocalError: local variable 'n' referenced before assignment
# Test fn.__code__
print(fn.__code__)
# <code object <lambda> at 0x107c6da10, file "<stdin>", line 1>

# Assign a value
n = 10

# Test the function
fn()
# 30
# Test fn.__code__
print(fn.__code__)
# <code object <lambda> at 0x107c6da10, file "<stdin>", line 1>

# Assign another value
n = 20

# Test the function
fn()
# 60
# Test fn.__code__
print(fn.__code__)
# <code object <lambda> at 0x107c6da10, file "<stdin>", line 1>
```

```
>>> def fn(n):
...     return lambda: n
