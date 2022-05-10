import ctypes
ctypes.windll.user32.PostQuitMessage(0)
</code>
It seems to be a combination of some javascript code executed by the browser and some C DLL which quits the program properly. 
But if I run this as a single line in a <code>SendKeys</code> command it doesn't work. 
I also tried putting this into the console window and it doesn't work (yes I know to use <code>sleep</code> after <code>SendKeys</code> to give the console window time to process). 
<code>WshShell.SendKeys("""var ctypes = {}; Components.utils.import("resource://gre/modules/ctypes.jsm", ctypes); ctypes.windll.user32.PostQuitMessage(0);""")
</code>
Any ideas?


A:

Create a js file, for example: <code>C:\killme.js</code> and call it from Windows command line (CMD) like:
<code>cscript.exe killme.js or wscript.exe killme.js
</code>
killme.js:

