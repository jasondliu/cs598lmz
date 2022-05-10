from lzma import LZMADecompressor
LZMADecompressor()
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\danie_000\Documents\Python\venv\lib\site-packages\lzma\lzmamodule.py",
  line 34, in <module>
    raise ImportError("No module named '_lzma'")

ImportError: No module named '_lzma'
```

I downloaded the [pylzma package](https://pypi.org/project/pylzma/) and 
installed it into my python virtual environment via:

```
.\venv\Scripts\pip.exe install pylzma
```

Then:

```
>>> from lzma import LZMADecompressor
>>> LZMADecompressor()
<lzma.decompress.LZMADecompressor object at 0x03890A48>
```

The properties, `file` and `check`, of the decompressor
