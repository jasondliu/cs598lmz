from types import FunctionType
list(FunctionType(lambda: None, globals(), "lambda_function"))


a = [1, 2, 3]
b = a
id(a) == id(b)
id(a) == id(a)
id(a) == id(a[:])

True == 1
False == 0

[1, 2] + [3, 4]
(1, 2) + (3, 4)
"Hello" + " " + "World!"

"hello" * 5

[1, 2] * 5

(1, 2) * 5

[None] * 5

(None,) * 5

[None] * 3 + [1, 2]

2 in [1, 2, 3]

2 not in [1, 2, 3]

a = [1, 2, 3]
a[0]
a[-1]

a = [1, 2, 3, 4, 5]
a[1:3]

a = [1, 2, 3, 4, 5]
a[1:3] = [9, 10]
a


