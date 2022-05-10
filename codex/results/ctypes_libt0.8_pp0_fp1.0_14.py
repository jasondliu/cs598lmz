import ctypes
ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), ctypes.py_object(Exception))
self.my_threads[thread_id]._Stop()
</code>
and in the thread:
<code>def _Stop(self):
    self._Thread__stop()
</code>
but it doesn't work (the thread never exits).
If I try to do in the "main" class:
<code>ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), ctypes.py_object())
</code>
I get:
<code>ValueError: NULL PyThreadState
</code>
It is strange, because the thread state is not NULL (I can access it by <code>sys._current_frames()[thread_id]</code>).


A:

If you want to stop one thread, you should create a <code>Thread</code> instance for that thread, and then you call <code>Thread.join()</code>.
A code snippet, as example:
<code>#
