import lzma
# Test LZMADecompressor.
decompressor = lzma.LZMADecompressor()
with open('enwik8.xz', 'rb') as f:
    file_content = f.read()
    data = decompressor.decompress(file_content)
    text = data.decode('utf-8')

print('Read %d characters' % len(text))

fp = open("enwik8_uncompressed.txt",'w')
fp.write(text)
fp.close()

print('Saved to enwik8_uncompressed.txt')
 
# Open the file
with open('enwik8_uncompressed.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print('corpus length:', len(text))

chars = sorted(list(set(text)))
print('total chars:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumer
