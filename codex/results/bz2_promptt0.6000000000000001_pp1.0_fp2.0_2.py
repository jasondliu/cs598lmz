import bz2
# Test BZ2Decompressor
with open('enwiki-latest-pages-articles.xml.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda : f.read(100 * 1024), b''):
        text = decompressor.decompress(block)
        if text:
            print(text.decode('utf-8')[:100])
            break

# Test BZ2File
with bz2.BZ2File('enwiki-latest-pages-articles.xml.bz2') as f:
    print(f.read(200).decode('utf-8'))

# Test bz2.open()
with bz2.open('enwiki-latest-pages-articles.xml.bz2', 'rt') as f:
    print(f.read(200))

# Test bz2.compress()
original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)
compressed = bz2.compress(original
