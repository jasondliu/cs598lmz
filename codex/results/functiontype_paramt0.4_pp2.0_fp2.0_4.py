from types import FunctionType
list(FunctionType(lambda: 1, globals(), "lambda").__closure__)[0].cell_contents
</code>

