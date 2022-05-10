import lzma
lzma.decompress(buf["code"])

# osx
import gzip
import io
gzip.GzipFile(fileobj=io.BytesIO(buf['code'])).read()
str(buf['code'])

# freebsd
# requires python3-base
import bz2
bz2.decompress(buf['code'])

# pux 
# ubuntu python3 does not include zlib
import zlib
zlib.decompress(buf['code'])

# ubuntu python2 does not include zlib or zopfli
import zopfli
zopfli.decompress(buf['code'])

# ubuntu python3 does not include zopfli
import zopfli
zopfli.decompress(buf['code'])

# windows
# requires python3-base
import lzma
lzma.LZMADecompressor().decompress(buf["code"])

# need to figure out pyinstaller import magic
import zipfile
zf = zipfile.
