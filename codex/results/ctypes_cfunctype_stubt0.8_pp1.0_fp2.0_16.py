import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hey"
print fun()
</code>
This works fine and prints <code>"hey"</code>, but when I tried the same thing with a function that returns an <code>std::string</code>, like <code>std::string()</code>, it crashed with an access violation. I also tried <code>std::string("asd")</code> but that crashed, too. I've looked at Boost.Python's <code>str_function</code> object to see what I'm doing wrong, but couldn't find anything. Can anyone help me?

