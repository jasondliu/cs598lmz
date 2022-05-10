import _struct
# Test _struct.Struct
<code>&gt;&gt;&gt; print _struct.Struct('@x').size
0
</code>
Python bug: https://bugs.python.org/issue20954
EDIT:
I've determined that the problem is not in _struct.py but with the code I wrote to convert a string to a value.
Error in code:
<code>def convert_string(self, value, format):
    '''
    Convert string in format to its corresponding value
    format: '@x' etc
    '''
    # Initialize value
    if value == '':
        value = 0
    try:
        # Convert string to value
        value = _struct.unpack(format, value)[0]
    except: # Never do this
        # ToDo: If error, then convert to correct type
        # value = [c for c in value]
        value = ord(value)
    return value
</code>


A:

I fixed the error by replacing <code>_struct.unpack()</code> with custom code.
<code>&gt;&gt;&
