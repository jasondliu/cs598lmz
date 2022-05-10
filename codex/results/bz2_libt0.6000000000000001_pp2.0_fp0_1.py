import bz2
bz2.decompress(img)

# decompress the file
f = bz2.BZ2File('img.bz2')
data = f.read()

# load the decompressed data
img = Image.open(io.BytesIO(data))
img

# load the file using the codecs library
import codecs
with codecs.open('img.bz2', 'rb') as f:
    data = f.read()

# load the decompressed data
img = Image.open(io.BytesIO(data))
img

# load the file using the codecs library
import codecs
with codecs.open('img.bz2', 'rb') as f:
    data = f.read()

# load the decompressed data
img = Image.open(io.BytesIO(data))
img

# load the file using the codecs library
import codecs
with codecs.open('img.bz2', 'rb') as f:
    data = f.read()

# load the decompressed data
img = Image.open(io.Bytes
