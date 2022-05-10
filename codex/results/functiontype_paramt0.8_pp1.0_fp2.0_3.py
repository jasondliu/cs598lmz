from types import FunctionType
list(FunctionType(lambda s: s, globals(), 'foo', ()) for x in range(5))
</code>
<code>list(gen())</code> creates a list of generators.  Of course, nothing ever calls <code>next()</code> on them.  They are not bound to the name <code>x</code>, so they are eligible for garbage collection.  They never fill the list, and then they are thrown away.

