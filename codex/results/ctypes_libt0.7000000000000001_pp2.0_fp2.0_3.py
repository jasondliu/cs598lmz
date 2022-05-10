import ctypes
ctypes.windll.user32.MessageBoxW(0, "Message", "Title", 1)

import ctypes
ctypes.windll.user32.MessageBoxA(0, "Message", "Title", 1)
</code>
It is not necessary to specify the Unicode or Ansi encoding if you are using Python 3.

