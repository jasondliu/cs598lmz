import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return None
dis(fun.__code__.co_code)
</code>
Output (Python 3.8):
<code>b'|\x00|\x01\x17\x83k\x83|\x03S'
</code>
Looks like a way to return <code>None</code>, but no clue about the <code>|\x00</code> and <code>|\x01</code>.
Detailed disassembly
Well, inspecting bytecodes with <code>dis</code> is never easy to follow, all the more if you're using it in a Python terminal and going through all the debug information it adds, so here's a fiddle to get the full disassembly, quite similar to what <code>dis</code> gives you, without all the confusing names that get in the way.
Now, keep in mind that the native representation of a code object is not necessarily the same as the Python description of it, so you'll have to decode a lot of it manually. So, let's look at <code>fun.__code__</code> in detail.
<code>&gt;&gt;&gt;
