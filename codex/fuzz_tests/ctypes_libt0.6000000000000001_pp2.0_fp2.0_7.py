import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, "D:\Personal\[FreeCourseSite.com] Udemy - The Python Mega Course Build 10 Real World Applications.torrent" , 0)
</code>
But, I'm getting the following error message.
<code>ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: wrong type
</code>
I'm curious about what is wrong with the code, and how to fix it. Any help would be appreciated.


A:

You need to pass <code>ctypes.wintypes.LPCWSTR</code> as the third argument to <code>SystemParametersInfoW</code>.
Alternatively, you can use <code>SystemParametersInfoA</code> with <code>ctypes.c_char_p</code>.

