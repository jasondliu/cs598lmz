import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_float)

def func():
    print("Hello World")

func_ptr = FUNTYPE(func)

lib.call_me(func_ptr)
</code>
This throws a segmentation fault.
EDIT:
I think I've finally figured out the problem.  The error was in the cpp code, not the python code.  I had the following:
<code>typedef void (*func_ptr_t)(void);

void call_me(func_ptr_t func)
{
    func();
}
</code>
when I should have been doing this:
<code>typedef void (*func_ptr_t)();

void call_me(func_ptr_t func)
{
    func();
}
</code>

