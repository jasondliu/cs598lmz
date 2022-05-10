from types import FunctionType
list(FunctionType(f1.func_code, globals(), "func_with_closure")())
</code>
But I wanted to recreate the whole function <code>f1</code> with its closure.

