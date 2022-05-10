import lzma
lzma.decompress(data)

#lzma.LZMADecompressor().decompress(data)

 
#print(data)
#print(data.decode('unicode_escape'))
#data.decode('unicode_escape')
#print(data.decode('utf-8'))

#lines = data.decode('unicode_escape').splitlines()
#print(lines[2])
#line = lines[2]
#print(line)

#import lzma

#with open('/tmp/data.xz', 'rb') as f:
#    data = f.read()
#
#data = lzma.decompress(data)
#
#for line in data.decode('utf-8').splitlines():
#    print('line: {}'.format(line))
