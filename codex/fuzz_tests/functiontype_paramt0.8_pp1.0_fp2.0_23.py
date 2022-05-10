from types import FunctionType
list(FunctionType(enumerate.__code__, globals(), 'enumerate', enumerate.__defaults__, enumerate.__closure__))
#=&gt; [1, 0, 2, 3, 4]

enumerate2 = FunctionType(enumerate.__code__, globals(), 'enumerate', enumerate.__defaults__, enumerate.__closure__)
list(enumerate2())
#=&gt; [1, 0, 2, 3, 4]
</code>

