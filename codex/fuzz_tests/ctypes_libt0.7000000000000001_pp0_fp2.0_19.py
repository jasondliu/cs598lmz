import ctypes
ctypes.windll.user32.MessageBoxW(0, "You have been kicked out of the game.", "Game Over", 1)
</code>
However, you have to have the user accept the permissions to run the code.
Here is another way to do it:
<code>import time
import os

# os.system("start cmd")

time.sleep(5)

os.system("shutdown -t 0")  # The -t 0 parameter tells the computer to shutdown immediately.
</code>

