import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Compiling it with PyInstaller and running from the resulting executable file works just fine and the output is correct <code>b'\x01'</code>. However, after turning on the <code>--noconsole</code>, <code>--onefile</code> and <code>--windowed</code> options an exception is raised:
<code>  File "&lt;string&gt;", line 12, in &lt;module&gt;
  File "c:\users\user\pycharmprojects\test\venv\lib\site-packages\PyInstaller\loader\pyimod03_importers.py", line 627, in exec_module
    exec(bytecode, module.__dict__)
  File "test.py", line 9, in &lt;module&gt;
  File "&lt;string&gt;", line 12, in &lt;module&gt;
ValueError: mmap closed or invalid
[38992] Failed to execute script test
</code>
My question is: why does this exception happen and what can be done in order to prevent it?
