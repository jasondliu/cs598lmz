import lzma
lzma.open('./download/t.txt.xz').read()

import json
with open('./download/t.json', 'r') as f:
	print(json.load(f))

import pickle
with open('./download/t.pickle', 'rb') as f:
	print(pickle.load(f))

print(hashlib.md5(b'123456').hexdigest())
print(hashlib.sha1(b'123456').hexdigest())
print(hashlib.sha256(b'123456').hexdigest())
print(hashlib.sha512(b'123456').hexdigest())

print(os.path.abspath('.'))
print(os.path.join('/home/xgw', 'testdir'))
print(os.mkdir('./testdir'))
print(os.rmdir('./testdir'))

print(os.path.split('/home/xgw/test.txt'))
print(os.path.splitext('/
