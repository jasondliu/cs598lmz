from types import FunctionType
list(FunctionType(lambda: None, {}).__closure__) # will return a list containing None
</code>

