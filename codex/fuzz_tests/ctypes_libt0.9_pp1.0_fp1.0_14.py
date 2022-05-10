import ctypes
ctypes.windll.user32.MessageBoxW(0, "done", "title", 1)
</code>
replace the MessageBoxW with another function and it breaks. I've tried MessageBoxA, GetWindowText and a few others, they all seem to break it.
When I try it on a fresh machine it works, but then on the dev machine I do a "find" in the system folder and search for "Get", and get c:\windows\system32\msctf.dll, which is obviously the right one. But then I go to that file, and it doesn't work. Neither does saving GetWindowTextW to a file and loading that up in my script - it throws an error.
So what is happening?
edit: I've also tried it in Python 2.7 and it works, but then I do an import windll, it breaks with an unloadable library
edit: I believe I have figured it out... the first time I call "GetWindowTextW" (not exactly the same syntax but the same story for GetWindowTextA) the script works. But then, somehow the fact that I have called this function somehow breaks the script, and it can't
