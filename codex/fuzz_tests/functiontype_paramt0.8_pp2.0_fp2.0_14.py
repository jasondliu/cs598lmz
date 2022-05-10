from types import FunctionType
list(FunctionType(code, globals()) for code in code_objects)
</code>

But I get the following error, just pointing to the first line:
<code>_pickle.PicklingError: Can't pickle &lt;function &lt;lambda&gt; at 0x7f0f4b4a4b90&gt;: it's not found as __main__.&lt;lambda&gt;
</code>
I tried to insert the code below (variable <code>code_objects</code> is a list of code objects in both cases) and it works, but it's not an efficient way to proceed.
<code>list(FunctionType(code, globals()) for idx, code in enumerate(code_objects))
</code>
Do you know what am I missing?
I can't post all the code, but I can try to show it in a more complete example.
<code>import pickle
import collections

def run_code(code):
    return lambda: eval(code, globals())

code_object = compile('a + 1', '&lt;string&gt;', '
