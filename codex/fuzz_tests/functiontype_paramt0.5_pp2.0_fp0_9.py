from types import FunctionType
list(FunctionType(lambda:0,globals(),'foo') for i in range(2))
</code>

