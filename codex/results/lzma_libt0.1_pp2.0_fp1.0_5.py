import lzma
lzma.LZMAError:
  File "/usr/lib/python3.6/lzma.py", line 6, in &lt;module&gt;
    from _lzma import *
ModuleNotFoundError: No module named '_lzma'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3.6/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/usr/lib/python3.6/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/home/pi/Desktop/Python/test.py", line 1, in &lt;module&gt;
    import lzma
  File "/usr/lib/python3.6/lzma.py", line 8, in &lt;module&gt;
    raise ImportError("This module requires the xz/lzma file format")
ImportError: This module requires the x
