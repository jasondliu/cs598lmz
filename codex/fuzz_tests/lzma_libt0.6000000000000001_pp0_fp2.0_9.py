import lzma
lzma.decompress(dat)
 

#2. bz2
import bz2
bz2.decompress(dat)

#3. gz
import gzip
gzip.decompress(dat)

#4. zlib
import zlib
zlib.decompress(dat)

#5. lz4
import lz4
lz4.block.decompress(dat)

#6. lzw
import lzw
lzw.decompress(dat)

#7. lzham
import lzham
lzham.decompress(dat)

#8. snappy
import snappy
snappy.decompress(dat)

#9. brotli
import brotli
brotli.decompress(dat)

#10. zstd
import zstd
zstd.decompress(dat)

#11. lz4
import lz4
lz4.frame.decompress(dat)

#12. blosc
import blosc
bl
