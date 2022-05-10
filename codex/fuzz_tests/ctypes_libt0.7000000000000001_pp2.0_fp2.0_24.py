import ctypes
ctypes.windll.user32.MessageBoxW(0, "Error: " + str(e), "Error", 1)
</code>
but it is showing error as
<blockquote>
<p>Traceback (most recent call last):
    File "C:\Users\HP\Documents\Python Scripts\Scratchpad.py", line 1, in 
      import sys
    File "C:\Users\HP\Documents\Python Scripts\Scratchpad.py", line 2, in 
      import ctypes
    File "C:\Users\HP\Documents\Python Scripts\ctypes.py", line 1, in 
      import ctypes
  ImportError: No module named ctypes</p>
</blockquote>
please help..i am a beginner


A:

<code>from ctypes import *
windll.user32.MessageBoxA(0, "Error: " + str(e), "Error", 1)
</code>

