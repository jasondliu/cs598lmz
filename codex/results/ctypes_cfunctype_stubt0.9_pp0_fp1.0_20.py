import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    temp = 10
    print("value of bug is :{}".format(bug))
    print("value of temp is :{}".format(temp))
    return 0

if __name__ == '__main__':
    cmp_callback = fun
    cmp_callback()
</code>
here i am getting output as :
<code>value of bug is :20
value of temp is :10
</code>
here i am getting output for temp as i have defined inside the function but i dont have defined item bug in global it is defined inside the function also..
And when i remove global bug from function it shows 'bug' not defined.
both case why is it showing value of bug?
what is happening here?


A:

<code>@FUNTYPE</code> makes <code>fun</code> a function that runs in the CPython interpreter, with the interpreter throwing a <code>NameError</code> instead of the code you compiled, because the compiled code doesn't contain any global value for the name <code>bug</code>.

