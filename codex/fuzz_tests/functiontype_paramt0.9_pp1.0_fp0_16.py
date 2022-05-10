from types import FunctionType
list(FunctionType(getattr(math, 'sin'), globals(), 'sin'))
# [<function math.sin>]
list(FunctionType(getattr(math, 'sin'), {'math': math}, 'sin'))
# [<function <lambda>>]
```
The second argument to `FunctionType()` is the `__globals__` for the new function (not the same as `globals()`), and the third argument is the function's `__name__`.

For example, `FunctionType()` can be used to enforce a singleton pattern:

```python
def singleton(cls):
	def getinstance(*args, **kwargs):
		if not cls.instance:
			cls.instance = cls(*args, **kwargs)
		return cls.instance
	return FunctionType(getinstance.__code__, cls.__globals__, cls.__name__, cls.__defaults__, cls.__closure__)
	
class Spam:
	instance = None
	def __init__(self):

