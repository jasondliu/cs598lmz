fn = lambda: None
# Test fn.__code__
In [329]: c = fn.__code__                                                                               
In [330]: c                                                                                             
Out[330]: <code object &lt;lambda&gt; at 0x7ffdb13fa410, file "&lt;ipython-input-329-aca3673d445a&gt;", line 
    1&gt;
In [331]: c.co_argcount                                                                                
Out[331]: 0
In [335]: c.co_code                                                                                    
Out[335]: b's\x00'
In [336]: c.co_consts                                                                                  
Out[336]: (None,)
In [337]: c.co_varnames                                                                                
Out[337]: ()    
</code>
There's a whole collection of functions to dissect and interpret code objects (at a python source level): https://docs.python.org/3/library/dis.html.
<code>In [343]: decode_instruction(c.co_code)                                                                
Out[343]: CodeInfo(opcode=
