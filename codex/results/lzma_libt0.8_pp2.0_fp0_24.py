import lzma
lzma.LZMAError: error while decompressing data: The data is corrupt
</code>


A:

Use the built-in <code>zipfile</code> module to unpack the zipfile contents into a directory in memory, then read and parse them from there.
<code>import os, zipfile, io

zf = zipfile.ZipFile(io.BytesIO(contents))

# construct a directory with the same name as the original file
with zipfile.ZipFile(io.BytesIO(contents), 'r') as zf:
    for info in zf.infolist():
        dname = os.path.dirname(info.filename)
        if dname:
            os.makedirs(dname)

for fn in zf.namelist():
    if fn.endswith('.xml'):
        with lxml.etree.parse(os.path.join(zf.filename, fn)) as tree:
            # work with the XML tree
</code>

