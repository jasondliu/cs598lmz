import ctypes
ctypes.CDLL("/System/Library/TCC/TCC")
import pip
</code>
I get the error field:
<code>$ pip install gevent
Downloading/unpacking gevent
Downloading gevent-1.1.1.tar.gz (987kB): 987kB downloaded         
Running setup.py egg_info for package gevent
    Traceback (most recent call last):
      File "&lt;string&gt;", line 16, in &lt;module&gt;
      File "/private/var/folders/5c/39pbpz_j10j26h_y8wc5f7vh0000gn/T/pip-build-mF9fO5/gevent/setup.py", line 439, in &lt;module&gt;
        **kw
      File "/Library/Python/2.7/site-packages/setuptools/__init__.py", line 10, in &lt;module&gt;
        import setuptools.version
      File "/Library/Python/2.7/site-packages/setuptools/version.
