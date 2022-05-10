import io
# Test io.RawIOBase
with io.open('hello.txt', 'rb') as f:
    print(f.readline().decode())

with io.FileIO('hello.txt') as source:
    with io.FileIO('hello-copy.txt', 'w') as target:
        while True:
            buffer = source.read(16384)
            if not buffer:
                break
            target.write(buffer)

with open('hello.txt') as f:
    print(f.readline())

with open('hello.txt', 'rb') as f:
    print(f.readline().decode())

file_like_object = io.StringIO()
print(file_like_object.write('hello'))
print(file_like_object.write(' world'))
print(file_like_object.seek(0))
print(file_like_object.read())
print(file_like_object.close())

file_like_object = io.StringIO('some data')
print(file_like_object.readline())
print(file_like_
