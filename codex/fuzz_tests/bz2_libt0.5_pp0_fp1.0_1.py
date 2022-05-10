import bz2
bz2_file = bz2.BZ2File("../data/enwik9.bz2")
data = bz2_file.read()
bz2_file.close()

print("data[:4] =", data[:4])
print("data[-4:] =", data[-4:])

print("len(data) =", len(data))

print("data.count(b'Wikipedia') =", data.count(b"Wikipedia"))

print("data.split()[:10] =", data.split()[:10])

import re
pattern = re.compile(b"^(=+)\s*(.*?)\s*=+$", re.MULTILINE)
for match in pattern.findall(data):
    print("{0:.<20s}{1:.>20s}".format(match[1], match[0]))

from collections import Counter

words = data.split()
print("len(words) =", len(words))

counts = Counter(words)
print("counts[\"
