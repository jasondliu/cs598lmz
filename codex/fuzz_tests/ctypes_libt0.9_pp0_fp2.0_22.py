import ctypes
ctypes.windll.user32.SetProcessDPIAware()
</code>
I tried to insert this code in the following locations:

<code>main.py</code>
<code>start.py</code>
<code>screen.py</code> 

None of the above locations solved my problem. 
Is there some procedures that I need to do before I insert my code in the above locations? Or have I gone to the wrong location?

