from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda') for _ in range(2))
# [<function <lambda> at 0x7fbbbd26b6e0>, <function <lambda> at 0x7fbbbcac3020>]
# Inline for comprehension
type(FunctionType(lambda: None, globals(), 'lambda'))
# <class 'function'>
new_id = [FunctionType(lambda: None, globals(), f'lambda_{i}') for i in range(1, 3)]
# [<function <lambda_1> at 0x7fbbbd058ae0>, <function <lambda_2> at 0x7fbbbd058d00>]
type(FunctionType(lambda: None, globals(), 'lambda_1'))
# <class 'function'>
```

```python
# Regular lambdas
(lambda: None)()
# None
(lambda: print(1))()
# 1

# Inline lambdas
list(lambda: None for _ in range(2))
# [<function <lambda> at 0x7fbbbd
