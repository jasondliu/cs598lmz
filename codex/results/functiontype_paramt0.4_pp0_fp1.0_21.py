from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_freevars)

# Output:
# ['None']
</code>

