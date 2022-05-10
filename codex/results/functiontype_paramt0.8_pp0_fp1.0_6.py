from types import FunctionType
list(FunctionType(lambda: None).__annotations__)

# in Python 2.6, using tensorflow_version 1.14, the output was
# ['b', 'c', 'a']

# in Python 2.6, using tensorflow_version 1.15, the output was
# ['b', 'c', 'd', 'e', 'a']
</code>

