import lzma
lzma.open()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "C:\Python27\lib\lzma.py", line 12, in &lt;module&gt;
    from _lzma import *
ImportError: DLL load failed: The specified module could not be found.
</code>
I have tried to install the pylzma package but I get the same error.
I have also tried to install the pyliblzma package but I get the following error:
<code>C:\Python27\lib\distutils\dist.py:267: UserWarning: Unknown distribution option: 'long_description_content_type'
  warnings.warn(msg)
running install
running build
running build_ext
building '_lzma' extension
error: Unable to find vcvarsall.bat
</code>
I have tried to install the pyliblzma package from the command line but I get the same error.

