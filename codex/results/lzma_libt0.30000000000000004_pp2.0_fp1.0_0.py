import lzma
lzma.LZMAError:
  File "/usr/lib/python3.6/lzma.py", line 6, in &lt;module&gt;
    from _lzma import *
ModuleNotFoundError: No module named '_lzma'
</code>
I am using python 3.6.8 on Ubuntu 18.04.
I tried to install <code>_lzma</code> using <code>pip3</code> but it didn't work.
<code>$ pip3 install _lzma
Collecting _lzma
  Using cached https://files.pythonhosted.org/packages/e1/a0/a9a9d6f9d6f9a1a7c6f8a6e8a6e8a6e8a6e8a6e8a6e8a6e8a6e8a6e8a6e8/_lzma.cpython-36m-x86_64-linux-gnu.so
Installing collected packages: _lzma
Exception:
Traceback (most recent call
