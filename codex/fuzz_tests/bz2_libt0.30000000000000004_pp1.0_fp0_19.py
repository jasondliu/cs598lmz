import bz2
bz2.decompress(bz2.compress(data))

# zip
import zipfile
with zipfile.ZipFile('mydata.zip', 'w') as zf:
    zf.write('mydata.txt')

with zipfile.ZipFile('mydata.zip', 'r') as zf:
    print(zf.read('mydata.txt'))

# pickle
import pickle
mylist = ['a', 'b', 'c']
picklestring = pickle.dumps(mylist)
mylist2 = pickle.loads(picklestring)
print(mylist2)

# json
import json
json.dumps([1, 'simple', 'list'])

x = {'a': 1, 'b': 2, 'c': 3}
json.dumps(x)

json.dumps(x, indent=4, separators=(',', ': '))

json.dumps(x, indent=4, separators=(',', ': '), sort_keys=True)

json.loads('{"a
