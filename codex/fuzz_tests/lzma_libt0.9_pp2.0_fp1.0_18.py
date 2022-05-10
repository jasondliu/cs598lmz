import lzma
lzma.xz_decompress(open('file.xz').read())


import zlib
zlib.decompress(open('file.zz').read())

import snappy
snappy.uncompress(open('file.snappy').read())

import brotli
brotli.decompress(open('file.bro').read())


from libarchive import entry_from_file, memory_writer
with open('file.tar', 'rb') as fd:
    for e in entry_from_file(fd):
        e.read_data(memory_writer())


import libarchive.public


for entry in libarchive.public.memory_reader(open('file.tar', 'rb').read()):
    with entry.get_file_object() as f:
        print(f.read())
        print(entry.get_pathname())
        print(entry.get_size())


import json

from libarchive.public import memory_reader
from libarchive.public import memory_writer

with memory_reader(b'{"name": "test"}
