from types import FunctionType
list(FunctionType(lambda: 0, globals(), 'foo') for x in range(10**9))
</code>
So it's OOMing for me at about <code>10**6</code>.
I think this is more a demonstration of how bad Python's lambdas are than a demonstration of how bad Python's generators are.

