import ctypes
ctypes.windll.user32.LockWorkStation()
</code>
However, I get the following error:
<blockquote>
<p>OSError: [WinError 126] The specified module could not be found</p>
</blockquote>
I've tried using <code>ctypes.cdll.LoadLibrary("user32")</code> as well as <code>ctypes.cdll.LoadLibrary("user32.dll")</code>, but both return the same error.
I'm using Python 3.7.3 and Windows 10.

