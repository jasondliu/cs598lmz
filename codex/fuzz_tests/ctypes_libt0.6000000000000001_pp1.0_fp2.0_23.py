import ctypes
ctypes.windll.user32.LockWorkStation()
</code>
You can also do this:
<code>import subprocess
subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"])
</code>

