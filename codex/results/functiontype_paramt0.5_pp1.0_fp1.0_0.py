from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo"))
</code>
Output:
<code>['foo']
</code>

