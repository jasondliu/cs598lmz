import ctypes
ctypes.windll.user32.MessageBoxW(0, "You need to run this as administrator.", "Error", 1)
</code>
This may work:
<code>subprocess.call(["cmd", "/c", "start", "announce.py"], shell=True)
</code>
This may not, but worth a try:
<code>subprocess.call(["powershell", "start", "announce.py"], shell=True)
</code>

