import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
It works fine, but it freezes the program. I want to run this code in a separate thread, so it won't freeze the program.
I tried this code:
<code>import threading
import ctypes

def messagebox():
    ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

threading.Thread(target=messagebox).start()
</code>
But it didn't work.
How can I run this code in a separate thread?


A:

You can use <code>ctypes.windll.user32.MessageBoxW</code> in a thread, but it will still block the thread until the user has dismissed the message box. 
The problem is that the message box is modal, which means that it prevents other windows from being accessed while it is visible. If you want to show a message box while your program continues to run, you will need to use a non-modal message box.

