import bz2
# Test BZ2Decompressor Object
with open('wiki_line.bz2', 'rb') as f:
    binary = f.read(10)
bz2_str = binary.decode('ISO-8859-1')
print(repr(bz2_str))
with open('wiki_line.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    
    data = []
    while True:
        file_block = f.read(100)
        if not file_block:
            break
            
        stream_data = decompressor.decompress(file_block)
        if not stream_data:
            continue
        data.append(stream_data.decode('utf-8'))

wiki_article = '\n'.join(data)
print(wiki_article[:2000])

with open('wiki_line.bz2', 'rb') as f:
    for line in bz2.BZ2File(f):
        print(line)
        break

 
# Compressing Data
with open('
