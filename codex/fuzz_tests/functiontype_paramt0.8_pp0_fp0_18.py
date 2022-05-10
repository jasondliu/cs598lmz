from types import FunctionType
list(FunctionType(code, {}, '_converter'))(d)

# Result:
#
#     [{'one' : 1, 'two' : 'dos', 'three': True},
#      {'one' : '1', 'two' : 'dos', 'three': True},
#      {'one' : 1, 'two' : 2, 'three': True},
#      {'one' : '1', 'two' : 2, 'three': True}]
</code>
To get the converter function for a given dictionary D,
<code>code = compile(D.__repr__(), '&lt;args&gt;', 'eval')
</code>
or
<code>code = compile(D.__dict__.__repr__(), '&lt;args&gt;', 'eval')
</code>
Use <code>D.__repr__()</code> if <code>D</code> is a dict, or use <code>D.__dict__.__repr__()</code> if <code>D</code> is an instance of a class
