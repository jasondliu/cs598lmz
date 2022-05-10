from types import FunctionType
list(FunctionType(lambda x: x, globals())("abc"))
</code>
I also tried to use <code>inspect</code> module, but it shows me only function name, not its body.
Is it even possible to get function body as a code string?


A:

<code>&gt;&gt;&gt; import inspect
&gt;&gt;&gt; inspect.getsource(lambda x: x)
'lambda x: x\n'
</code>

