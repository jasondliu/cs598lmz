from types import FunctionType
list(FunctionType(f1.__code__, f1.__globals__, name=f1.__name__,
                  argdefs=f1.__defaults__,
                  closure=f1.__closure__).__globals__)
</code>
list of you function
<code>f1.__closure__
</code>
That's right, but you will have errors, sicne <code>__closure__</code> is <code>None</code>

