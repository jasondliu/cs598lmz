import lzma
lzma.decompress(archivo_comprimido)

#%%

import zlib

compresor = zlib.compressobj()
descompresor = zlib.decompressobj()

archivo_comprimido = compresor.compress(texto)
archivo_comprimido += compresor.flush()
archivo_comprimido

descompresor.decompress(archivo_comprimido)


#%%

from bz2 import BZ2Compressor, BZ2Decompressor

compresor = BZ2Compressor()
descompresor = BZ2Decompressor()

archivo_comprimido = compresor.compress(texto)
archivo_comprimido += compresor.flush()
archivo_comprimido

descompresor.decompress(archivo_comprimido)
