import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def fun2():
    return "hello too"

if test(fun) == "hello":
    print("test ok")
if test2(fun2) == "hello too":
    print("test2 ok")
</code>
this is my swig file:
<code>%module test
%{
extern "C" char* test(void* fun);
extern "C" char* test2(void (*)(void));
%}
extern "C" char* test(void* fun);
extern "C" char* test2(void (*)(void));
</code>
While running this i get the following error
<code>/usr/local/bin/swig -python -py3 -c++ test.i
/usr/local/bin/swig -python -py3 -c++ test.i
/usr/local/bin/swig -python -py3 -c++ test.i
/usr/local/bin/swig -python -py3 -c++ test.i
/usr/local/bin/swig -python -
