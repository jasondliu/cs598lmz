from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda').__code__.co_freevars)

# Output:
# ['None']
</code>

