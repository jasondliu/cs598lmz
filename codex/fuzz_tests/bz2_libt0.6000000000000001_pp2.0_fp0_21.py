import bz2
bz2_file = bz2.BZ2File('test.log.bz2', 'w')
bz2_file.write(test)
bz2_file.close()

# Чтение
bz2_file = bz2.BZ2File('test.log.bz2', 'r')
bz2_file.read()
bz2_file.close()

# С помощью модуля zlib
import zlib
zlib_file = zlib.compress(test)
zlib.decompress(zlib_file)

# Сжатие с помощью gzip
import gzip
gzip_file = gzip.GzipFile('test.log.gz', 'w')
gzip_file.write(test)
gzip_file.close()

# Чтение
gzip_file = gzip.GzipFile('test.log.gz', 'r')

