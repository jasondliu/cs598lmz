import lzma
# Test LZMADecompressor
import sys
import os
import io
def _load_compressed_python_module(file, module_name):
    compressed = io.FileIO(file, 'rb')
    uncompressed = lzma.LZMADecompressor().decompress(compressed.read())
    code = marshal.loads(uncompressed[16:])
    module = imp.new_module(module_name)
    exec(code, module.__dict__, module.__dict__)
    sys.modules[module_name] = module
_load_compressed_python_module(os.path.join(os.path.dirname(__file__), '_compare_tools.cpython-37.pyc'), '_compare_tools')
from _compare_tools import *
# End test

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
	print("Usage: " + sys.argv[0] + " [--help | -h | [--skip-test-gen] source destination")
	sys.
