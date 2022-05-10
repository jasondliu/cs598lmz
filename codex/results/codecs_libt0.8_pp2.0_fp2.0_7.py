import codecs
codecs.encode(o, 'hex')

I get an error:
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape


A:

To encode a byte string to hex, use <code>bytes.hex()</code>:
<code>In [1]: b'hello'.hex()
Out[1]: '68656c6c6f'
</code>
To decode it back, you can use <code>bytes.fromhex()</code>:
<code>In [2]: bytes.fromhex('68656c6c6f')
Out[2]: b'hello'
</code>

