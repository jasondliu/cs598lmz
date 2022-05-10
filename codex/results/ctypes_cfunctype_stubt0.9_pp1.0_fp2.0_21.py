import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
</code>
raises the following exception
<code>&gt;&gt;&gt; import fun
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;frozen importlib._bootstrap&gt;", line 1558, in _handle_fromlist
  File "&lt;frozen importlib._bootstrap&gt;", line 1525, in _find_and_load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 586, in module_from_spec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 916, in create_module
  File "&lt;frozen importlib._bootstrap&gt;", line 222, in _call_with_frames_removed
TypeError: 'NoneType' object is not callable
</code>
I suppose this is because the frozen module is not a ModuleType but NoneType, both of the two following lines were executed successfully
<
