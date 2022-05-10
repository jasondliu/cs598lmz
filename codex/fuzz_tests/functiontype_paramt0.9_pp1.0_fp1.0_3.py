from types import FunctionType
list(FunctionType(l[0], globals())(*args) for args in l[1:])
</code>
Save the above code to a file and run it. Or use a Python interactive shell.

