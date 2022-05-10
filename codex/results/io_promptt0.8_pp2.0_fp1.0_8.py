import io
# Test io.RawIOBase.read1 
# https://hg.python.org/cpython/file/3.4/Modules/_io/fileio.c#l366
# https://hg.python.org/cpython/file/3.4/Modules/_io/bufferedio.c#l191

f = io.open('test_raw', 'wb')
f.write(b'a'*1024)
f.close()
f = io.open('test_raw', 'rb')
f.tell()

f.read1(3)
f.tell()
# Test io.TextIOWrapper.read1 
# https://hg.python.org/cpython/file/3.4/Modules/_io/textio.c#l2081

f = io.open('test_text', 'w', encoding='utf-8')
f.write(u'а'*1024)
f.close()
f = io.open('test_text', 'r', encoding='utf-8')
f.tell()

f.read1(3)
f
