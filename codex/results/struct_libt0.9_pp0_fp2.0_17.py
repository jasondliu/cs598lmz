import _struct
  File "/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/_struct.py", line 1, in &lt;module&gt;
    from _struct import *
ModuleNotFoundError: No module named '_struct'
</code>
It is installed via Homebrew and my python version is 3.6.4.


A:

In my case it was a problem of permissions. I just had to do:
<code>sudo chmod -R 755 /usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/
</code>
(where the number after python3 should be yours :))

