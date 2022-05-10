from types import FunctionType
list(FunctionType(lambda x,y:x+y, globals()) for x,y in [(1,2), (3,4)])

# [3, 7]
</code>

