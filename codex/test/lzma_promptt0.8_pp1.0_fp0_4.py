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
