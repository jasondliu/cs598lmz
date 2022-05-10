from types import FunctionType
list(FunctionType(func.__code__, globals(),
                  name=func.__name__,
                  argdefs=func.__defaults__,
                  closure=func.__closure__).__closure__)
</code>
You can also get just the value by accessing the cell object with index 0 (zero).

