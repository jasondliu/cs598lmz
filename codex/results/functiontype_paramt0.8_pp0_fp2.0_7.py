from types import FunctionType
list(FunctionType(lambda: lambda x: None, globals(), "foo"))() # None
</code>
More about functions:
http://docs.python.org/2/library/types.html#types.FunctionType
http://docs.python.org/2/reference/datamodel.html#the-standard-type-hierarchy

