import lzma
# Test LZMADecompressor
# http://stackoverflow.com/questions/22637000/python-3-lzma-decompress-decode

with open("wat.lzma", 'rb') as inp, lzma.open("wat.lzma", 'rb') as out:
    for line in inp:
        print(out.read())

d = lzma.LZMADecompressor()
d.decompress(b'wat.lzma')

#s = d.decompress(b'wat.lzma')
#print(s)

#with open('file.lzma', 'rb') as input, open('file.txt', 'w') as output:
#    output.write(input.read())

#f = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
#data = f.read()
#print(data)
#for line in f.readlines():
#    print(line)

#import pickle
#import lzma
