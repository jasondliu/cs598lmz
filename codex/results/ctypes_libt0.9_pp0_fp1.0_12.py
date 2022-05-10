import ctypes
ctypes.CDLL("libmylib.so", mode=ctypes.RTLD_GLOBAL)

import mylib

a = mylib.A("hello")
print("a.get_var1() is... %s" % a.get_var1())
print("a.get_var2() is... %s" % a.get_var2())

b = mylib.B("world")
print("b.get_var1() is... %s" % b.get_var1())
print("b.get_var2() is... %s" % b.get_var2())
</code>
testit.py prints "java world" as expected.
Note that I have to specify the mode=ctypes.RTLD_GLOBAL. If I omit this, python can import mylib OK but ctypes has no knowledege of libmylib.so which is necessary for resolving the vtable and hence it won't run.


A:

I solved this by changing the class definition to 
<code>class A(with_metaclass(Instruction, object)):
   
