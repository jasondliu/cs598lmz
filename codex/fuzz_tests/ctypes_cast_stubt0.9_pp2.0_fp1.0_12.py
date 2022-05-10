import ctypes
ctypes.cast(void_pointer, ctypes.py_object).value

http://ctypes.sourceforge.net/ctypes.html

class Command(object):
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def __call__(self, *args):
        self.function(*args)
</code>


A:

You can't use a <code>void*</code> in ctypes as-is; you have to first cast it to some type. I'm not very familiar with this part of ctypes, so I'll demonstrate how it's done in C:
<code>void foo(void);  // function that returns void
void foo(void) {
    // ...
}

void* foovar;    // datum of type void*

void bar(void);  // function that returns void
void bar(void) {
    void (*barfunc)(void) = foovar;  // cast foovar from type void* to type void (*)(void)
    barfunc();
}

// test code
int main
