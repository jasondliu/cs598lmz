import ctypes
ctypes.windll.user32.LockWorkStation()
</code>
The above code works fine but I want to run it in the background. I have tried to do the following:
<code>import ctypes

def lock():
    ctypes.windll.user32.LockWorkStation()

lock()
</code>
But it does not work.
What am I doing wrong?


A:

You have to call <code>lock()</code> in order for it to run.

