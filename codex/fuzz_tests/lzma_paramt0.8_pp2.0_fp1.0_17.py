from lzma import LZMADecompressor
LZMADecompressor()
</code>
But pyinstaller throws the following error:
<code>Traceback (most recent call last):
  File "foo.py", line 10, in &lt;module&gt;
  File "&lt;frozen importlib._bootstrap&gt;", line 983, in _find_and_load
  File "&lt;frozen importlib._bootstrap&gt;", line 967, in _find_and_load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 677, in _load_unlocked
  File "c:\users\user1\appdata\local\programs\python\python38-32\lib\site-packages\PyInstaller\loader\pyimod03_importers.py", line 493, in exec_module
    exec(bytecode, module.__dict__)
  File "site-packages\lzma.py", line 23, in &lt;module&gt;
  File "site-packages\lzma.py", line 19, in LZMADecompressor
