import bz2
bz2.compress(b'some data')

bz2.compress(b"Hello World!")

bz2.decompress(b'BZh91AY&SY\xc4\xac\x0c\x00\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# bz2.open is the same as regular open
bz2.open('lorem.txt.bz2', mode='wt')

# writing a compressed file
with bz2.open('lorem.txt.bz2', 'wt') as f:
    f.write('A line of text\n')

# reading a compressed file
with bz2.open('lorem.txt.bz2', 'rt') as f:
    text = f.read()
    print(text)
    print(text.split('\n'))
