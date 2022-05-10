import lzma
lzma.decompress(fileobj)

def decompress_xz_file(filename):
    with open(filename, 'rb') as f_in:
        with lzma.open(f_in, 'rt') as f_out:
            return f_out.read()
with open('sample.txt.xz', 'r') as f:
    text = f.read()
print(text)
text = decompress_xz_file('sample.txt.xz')
print(text)

with open('sample2.txt', 'r') as f:
    text = f.read()
with open('sample2.txt.xz', 'rb') as f:
    text_xz = f.read()
print(len(text), len(text_xz))

with open('sample.txt', 'r') as f:
    text = f.read()
with open('sample.txt.xz', 'rb') as f:
    text_xz = f.read()
print(len(text), len(text_xz))

import
