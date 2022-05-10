from types import FunctionType
list(FunctionType(*a).__code__.co_varnames for a in d)
</code>
Output:
<code>[['x'], ['x', 'y'], ['x', 'y'], ['x']]
</code>

