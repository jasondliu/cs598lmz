import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1024)
    print(m)

with open('test', 'r') as f:
    print(f.read())
    print(f.tell())
    print(f.seek(1))
    print(f.read())

with open('test', 'r') as f:
    print(f.readline())
    print(f.readline())

with open('test', 'r') as f:
    print(list(f))

import io

s = io.StringIO('')
s.write('hello')
print(s.getvalue())

s = io.StringIO('hello')
print(s.read())

s.truncate(2)
print(s.getvalue())

import json

d = {'a': 1, 'b': 2}
print(json.dumps(d, sort_keys=True, indent=4))

json_data = '''{
    "a": 1,
    "b": 2,
    "c": [
        {
            "d": 1
        },
        {
