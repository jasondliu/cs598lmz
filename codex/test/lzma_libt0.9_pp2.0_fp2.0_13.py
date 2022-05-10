import lzma
lzma_preset = getattr(lzma, 'FORMAT_XZ', None)
del lzma
import tokenize
