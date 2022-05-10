import ctypes
ctypes.cast(int(id(obj)), ctypes.py_object).value
</code>

And finally, where I really find this the most fun to use.  I run interactive code examples on my 3rd monitor with a shortcut key that sends the string to another python interpreter.  I capture mouse input and process it in my clipboard object.  This object acts as a shared memory object to pass between the two shells.
<code>#!/usr/bin/env python3

from pathlib import Path
import subprocess, shlex, os
from pynput.mouse import Button, Controller

# this_file = Path(__file__)
# parent_dir = this_file.parent
# clip_path = f'{parent_dir}/clip_server.py'
clip_path = 'clip_server.py'
clip_obj_name = 'clipboard'

class Clipboard:
    def __init__(self, path, clip_obj_name):
        self.path = path
        self.clip_obj_name = clip_obj_name

    def get(self):
        cmd = f'python {self
