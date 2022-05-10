import lzma
lzma.LZMAError('test')

try:
    import pylzma
    pylzma.LZMAError('test')
except ImportError:
    pass

