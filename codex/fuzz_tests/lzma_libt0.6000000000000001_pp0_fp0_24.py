import lzma
lzma.open()
</code>
But I get the following error:
<code>Traceback (most recent call last):
  File "C:/Users/User/PycharmProjects/untitled/untitled.py", line 1, in &lt;module&gt;
    import lzma
  File "C:\Users\User\PycharmProjects\untitled\venv\lib\site-packages\lzma.py", line 8, in &lt;module&gt;
    from _lzma import *
ImportError: DLL load failed: The specified module could not be found.
</code>
I'm using Windows 10 and Python 3.8.1.

