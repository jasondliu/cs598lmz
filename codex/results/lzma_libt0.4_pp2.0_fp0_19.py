import lzma
lzma.LZMAError:
  File "/usr/lib/python3.6/lzma.py", line 7, in &lt;module&gt;
    from _lzma import *
ImportError: /usr/lib/python3.6/lib-dynload/_lzma.cpython-36m-x86_64-linux-gnu.so: undefined symbol: LZ4F_createDecompressionContext
</code>
I'm using:

Ubuntu 18.04
Python 3.6.7
virtualenv 16.0.0
pip 18.1

I've tried the following:

Installing the <code>liblz4-dev</code> package
Reinstalling the <code>lz4</code> package
Reinstalling the <code>lzma</code> package

None of these have worked.
I don't want to install <code>lzma</code> in the system Python, because I don't want to break anything. I also don't want to install <code>lzma</code> in the virtualenv, because I don
