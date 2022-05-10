import lzma
lzma.LZMAError:
  File "/usr/lib/python3.7/lzma.py", line 6, in &lt;module&gt;
    from _lzma import *
ModuleNotFoundError: No module named '_lzma'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.7/site-packages/pip/_internal/commands/install.py", line 342, in run
    resolver.resolve(requirement_set)
  File "/usr/lib/python3.7/site-packages/pip/_internal/resolve.py", line 131, in resolve
    self._resolve_one(requirement_set, req)
  File "/usr/lib/python3.7/site-packages/pip/_internal/resolve.py", line 294, in _resolve_one
    abstract_dist = self._get_abstract_dist_
