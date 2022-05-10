import lzma
lzma.LZMAError:
  File "/usr/lib/python3.5/lzma.py", line 23, in &lt;module&gt;
    from _lzma import *
ImportError: /usr/lib/python3.5/lib-dynload/_lzma.cpython-35m-x86_64-linux-gnu.so: symbol __libc_res_nsearch version GLIBC_PRIVATE not defined in file libc.so.6 with link time reference
</code>
I'm running Ubuntu 16.04.


A:

I had the same issue, and solved it by installing liblzma via apt-get:
<code>sudo apt-get install liblzma-dev
</code>

