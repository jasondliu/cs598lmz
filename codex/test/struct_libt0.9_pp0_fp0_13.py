import _struct
import sys


# sz = 10485760
# sz = 8388608
# sz = 1073741824
sz = 4294967296
# sz = 4096
# sz = 8192
# sz = 16384
# sz = 32768
# sz = 16777216


print("writing,", sz)
start = time.time()
with open("/tmp/buffer", "wb") as fout:
    fout.write(b'A' * sz)
end = time.time()
print("duration,", end - start)


tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.write(b'C' * sz)
tmp.flush()

print("reading,", sz)
start = time.time()
with open("/tmp/buffer", "rb") as fin:
	while True:
		s = fin.read(sz)
		if s == b'':
			break
		# print(len(s))
