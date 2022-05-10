import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
I know ctypes is a ctypes library, but how do I fix this problem? And how could I change it so I don't have to use ctypes?
Sorry if this is a newbie question or if this question has already been asked, but I have tried to google this problem and it hasn't helped, so I am turning to the stackoverflow community.


A:

First install the pypiwin32 library, then use the below code:
<code>import win32gui

win32gui.MessageBox(0, 'Your text.', 'Your title.')
</code>
hackerman suggested a quick edit so this doesn't require the pypiwin32 package, https://stackoverflow.com/a/60297922/12694873
<code>import ctypes

ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>

