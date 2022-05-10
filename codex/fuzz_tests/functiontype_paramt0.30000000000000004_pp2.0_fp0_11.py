from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), 'add1')(i) for i in range(3))

# List comprehensions can contain complex expressions and nested functions:
[str(i) for i in range(10)]
[repr(i) for i in range(10)]
[i+i for i in range(10)]
[i for i in range(10) if i % 3 == 0]
[(i,j) for i in range(2) for j in range(3)]
[str(i) for i in range(10) if i % 3 == 0]
[i for i in range(10) if i % 3 == 0 or i % 5 == 0]
[i for i in range(20) if i % 3 == 0 or i % 5 == 0]
[i for i in range(20) if i % 3 == 0 or i % 5 == 0 if i % 7 == 0]
[i for i in range(20) if i % 3 == 0 or i % 5 == 0 if i % 7 == 0]
[i for i in range(20) if not i % 3 ==
