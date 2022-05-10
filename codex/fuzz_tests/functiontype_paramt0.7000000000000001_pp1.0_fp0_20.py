from types import FunctionType
list(FunctionType(lambda x: x, {}).__code__.co_freevars) == []
</code>
It seems like the <code>__code__</code> attribute is the key here, but I don't really understand it.
Can someone please explain how to determine whether a function is recursive?


A:

You can use the <code>inspect</code> module to get the functions <code>__code__</code> object and inspect the <code>co_code</code> attribute. The <code>co_code</code> attribute is the compiled code of the function as a string of bytes. The first byte of the string is <code>0x64</code> which is <code>LOAD_CONST</code> so we can assume the first argument to the function is a constant. The next byte is <code>0x5</code> which is <code>BINARY_SUBTRACT</code> so we can assume the function is <code>lambda x: x-1</code>.
By finding the <code>co_consts</code> we find that the function is <code>&lt;code object fact
