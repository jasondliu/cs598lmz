import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b"a" * n

f = File()
print(f.read(10))

import io
r = io.BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(r.read())

import pickle
d = dict(name='Bob', age=20, score=88)
# print(pickle.dumps(d))

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

import json
class Student(object):
    def __init__(self, name
