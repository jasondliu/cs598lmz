import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return " hello world "
print(fun)
print( str(fun() ) )
</code>
but I want to do this with a function that has parameters; the function I want to convert is 
<code>def fun(name, age ,gender ):
    return "hello " + name + " , you are " + age + " years old, and you are a " + gender
</code>
how can I do this?


A:

I found the solution, here it is:
<code>import ctypes

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.c_char_p , ctypes.c_char_p , ctypes.c_char_p)

@FUNTYPE
def fun(name, age ,gender ):
    return "hello " + name + " , you are " + age + " years old, and you are a " + gender

print(fun)
print( fun(b"John" , b"23" , b"man")  )
</code>

