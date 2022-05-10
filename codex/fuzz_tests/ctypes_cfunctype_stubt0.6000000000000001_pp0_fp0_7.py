import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

fun.__name__ = 'test'

def main():
    pass

if __name__ == '__main__':
    main()
</code>
And I got the error:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    main()
  File "test.py", line 9, in main
    fun.__name__ = 'test'
TypeError: __name__ must be set to a string object
</code>
But when I run the code:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print(fun.__name__)

def main():
    pass

if __name__ == '__main__':
    main()
</code>
I got the output:
<code>fun
</code>
As you can see, <code>fun.__name__</code> is a string object, so why I got the error
