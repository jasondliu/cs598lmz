from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.COMPRESSED_DATA)

# BytesIO, StringIO
# StringIO is for text
# BytesIO is for binary data

# from io import BytesIO
f = BytesIO()
f.write(b'abcdefg')
print(f.getvalue())
f.seek(0)
f.read(1)
f.read(2)

# from io import StringIO
s = StringIO('hello\nworld')
print(s.readline())
print(s.read())

# os.popen()
print(os.popen('ls -l').read())

# pickle
d = dict(name='Bob', age=20, score=88)
s = pickle.dumps(d)
print(s)
d = pickle.loads(s)
print(d)

f = open(r'D:\data\a.txt', 'wb')
pickle.dump(d, f)
f.close()
f = open(r'D:\data\a.txt', 'rb
