from types import FunctionType
list(FunctionType(f.__code__, globals(), "f").__closure__)

# Output:
# [&lt;cell at 0x101e7ffd8: int object at 0x101e7f6e0&gt;]
</code>

