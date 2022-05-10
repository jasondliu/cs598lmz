import types
types.ModuleType
dir(types)
dir(__builtins__)

import os
os.path.realpath("lsp.py")
os.path.abspath("lsp.py")
os.path.split("/root/lsp.py")
import re
re.sub('\s+', '-', 'test wer are')
import lsp
reload(lsp)

import lsp
lsp
"lsp"
lsp
lsp.__module__
lsp.__file__
lsp.__package__

import sys
sys.argv
for path in sys.path:
    print(path)

sys.path
sys.path.append("")
sys.path
del sys.path[-1]
sys.path

import sys
sys.path
sys.modules
sys.modules.keys()

for k in sys.modules.keys():
    print(k)
import imp
imp.find_module("lsp", ["."])

for path in sys.path:
    print(path)
