from lzma import LZMADecompressor
LZMADecompressor()
</code>
<blockquote>
<p>ModuleNotFoundError: No module named 'lzma'</p>
</blockquote>
The command <code>pip install python-lzma</code> or <code>pip install pylzma</code> do not work (see error messages below).
<code>pip install pylzma
</code>
<blockquote>
<p>ERROR: Command errored out with exit status 1:
       command: 'c:\users\ty\appdata\local\programs\python\python38-32\python.exe' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\Users\TY\AppData\Local\Temp\pip-install-hg1w885y\lzmaffi\setup.py'"'"'; <strong>file</strong>='"'"'C:\Users\TY\AppData\Local\Temp\pip-install-hg1w885y\lzmaffi\setup.py'"'"';f=getattr(tokenize,
