import ctypes
ctypes.windll.user32.MessageBoxW(0, "No user found", "Title", 1)
</code>
To get a handle to the parent window, I use <code>GetForegroundWindow()</code>, which can be done only if you #include <code>windows.h</code> using <code>#include "windows.h"</code> or <code>extern "C" { #include "windows.h" }</code>.
I used CLion to build the C program but I have no clue how to make a Windows executable file easily.
I tried to call <code>g++ ring.cpp -o ring</code> but it tells me
<blockquote>
<p>C:...\MinGW\bin\g++.exe: error: ring: No such file or directory</p>
</blockquote>
If it helps, CLion uses the following files:
<code>C:\Program Files\JetBrains\CLion 2019.1.4\bin\cmake\win\bin\cmake.exe
C:\Program Files\JetBrains\CLion 2019.1.4\bin\
