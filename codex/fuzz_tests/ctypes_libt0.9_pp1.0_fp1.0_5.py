import ctypes
ctypes.windll.shell32.ShellExecuteW(None, "open", url, None, None, 1)
</code>
And here is my setup.py:
<code>from cx_Freeze import setup, Executable

setup(name = "CryptPad" ,
        version = "0.1" ,
        description = "A cryptography tool pad" ,
        executables = [Executable("pad.py")])
</code>
I'm using python 3.3 & Windows Vista. 
I believe it has something to do with the fact that cx_Freeze creates a single exe file. 
Can you show what I'm doing wrong here please? :) 
Thanks!


A:

Just a guess, but maybe the <code>ShellExecute()</code> can't find the executable that you're trying to run. It might need a complete file path to the executable instead of just <code>'python'</code>.
The <code>sys.executable</code> property might be helpful here.

