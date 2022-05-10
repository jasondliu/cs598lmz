import lzma
lzma.LZMAError:
  File "/usr/lib/python3.8/lzma.py", line 5, in &lt;module&gt;
    from _lzma import *
ModuleNotFoundError: No module named '_lzma'
</code>
I have tried to install <code>_lzma</code> but it doesn't work.
<code>$ sudo apt-get install liblzma-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package liblzma-dev
</code>
I have tried to install <code>pylzma</code> but it doesn't work.
<code>$ sudo apt-get install pylzma
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package pylzma
</code>
I have tried to install <code>python3-lzma</code> but it doesn't work.
<code>$ sudo apt-get install python3-lzma
Reading package lists... Done
Building dependency tree
