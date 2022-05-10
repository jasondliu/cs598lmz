import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('hello')
    return 0x12345
ctypes.windll.user32.MessageBoxA(0, b"hello",
                                 b"it's a message!", 0)
</code>
The final line could actually be:
<code>ctypes.windll.user32.MessageBoxA(0, "hello".encode("mbcs"),
                                 "it's a message!".encode("mbcs"), 0)
</code>
Instead of <code>mbcs</code>, you could also use <code>latin-1</code>. It's the Windows system encoding.
In Python 2, the default <code>str</code> type is ASCII. If you pass an Unicode string to <code>ctypes</code>, <code>ctypes</code> will try to encode it to <code>mbcs</code> by default. In your script, 
<code>ctypes.windll.user32.MessageBoxA(0, "hello".encode("mbcs"),
                                 "it's a message!".encode("mbcs"), 0)
</code>
you are passing two bytes
