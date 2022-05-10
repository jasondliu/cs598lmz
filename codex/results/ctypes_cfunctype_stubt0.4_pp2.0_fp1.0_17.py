import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello, World!"

print(fun())
</code>
The above code works fine, but I want to return a list of strings.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ["Hello, World!", "How are you?"]

print(fun())
</code>
The above code gives the following error:
<code>Traceback (most recent call last):
  File "C:/Users/user/Desktop/test.py", line 5, in &lt;module&gt;
    print(fun())
  File "C:\Users\user\AppData\Local\Programs\Python\Python36\lib\ctypes\__init__.py", line 366, in __call__
    return self.call(args)
  File "C:\Users\user\AppData\Local\Programs\Python\Python36\lib\ctypes\__init__.py", line 361, in call
    return self.func(*args)
TypeError: must be real number, not list
