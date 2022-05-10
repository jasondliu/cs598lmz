import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
I have tried this, but it does not work.
<code>import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import os
os.system("python path/to/script.py")
</code>
I have tried this, but it does not work.
<code>import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import subprocess
subprocess.call("python path/to/script.py")
</code>
I have tried this, but it does not work.
<code>import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import subprocess
subprocess.Popen("python path/to/script.py")
</code>
I have tried this, but it does not work.
<code>import ctypes
ctypes.
