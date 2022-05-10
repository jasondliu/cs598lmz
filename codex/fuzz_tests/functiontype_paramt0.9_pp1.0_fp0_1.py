from types import FunctionType
list(FunctionType(test.__code__, globals()).__closure__)
</code>
Why does the first example fail. It seems like the missing <code>__closure__</code> attribute is the point that Python doesn't know how to look for the parent scope? 

