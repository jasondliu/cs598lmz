import io
class File(io.RawIOBase):
    def flush(self):
        pass
f = open('test.txt', mode='wb')
f.write(b'hello world')
f = open('test.txt', mode='rb')
f.read()
f = open('test.txt', mode='ab')
f.write(b'*' * 1000)
f = open('test.txt', mode='rb')
f.read()
f.close()
f.write(b'h')
f = open('test.txt', mode='wb')
f.close()
f.write(b'h')
f = open('test.txt', mode='wb')
f.flush()
f = open('test.txt', mode='wb')
f.fileno()
f.flush()
f = open('test.txt', mode='wb')
f = open('test.txt', mode='wb', buffering=0)
f = open('test.txt', mode='rb', buffering=1)
f = open('test.txt', mode='rb', buffering=1024)
f = open('test.txt', mode='rb
