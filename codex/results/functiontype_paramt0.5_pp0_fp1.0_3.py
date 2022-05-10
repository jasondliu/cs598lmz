from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), "lambda_function"))

# code objects
def func():
    pass
list(func.__code__)

# method-wrapper objects
list(list.append)

# module objects
list(sys)

# generator-iterator objects
list(x for x in range(10))

# memoryview objects
list(memoryview(b"abc"))

# dict-keyiterator objects
list({1: "a", 2: "b"}.keys())

# dict-valueiterator objects
list({1: "a", 2: "b"}.values())

# dict-itemiterator objects
list({1: "a", 2: "b"}.items())

# enumerate objects
list(enumerate("abc"))

# set objects
list(set("abc"))

# frozenset objects
list(frozenset("abc"))

# array.array objects
list(array.array("b", b"abc"))

# collections.deque objects
list(collections.deque("abc"))

# range objects

