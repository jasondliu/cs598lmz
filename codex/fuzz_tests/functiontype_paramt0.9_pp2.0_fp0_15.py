from types import FunctionType
list(FunctionType(fn, globals()['test']) for fn in [lambda this: this.foo(1)])
# ['23']
</code>

