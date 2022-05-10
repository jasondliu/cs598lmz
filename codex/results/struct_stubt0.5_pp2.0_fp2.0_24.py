from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

data = s.pack(1, False, 3.14159)
data

s.unpack(data)

import json

json.dumps([1,2,3,{'4': 5, '6': 7}])

with open('data.json', 'w') as f:
    json.dump(x, f)

json.dumps(False)

x = json.dumps(False)
x

x = json.loads(x)
x

x = json.dumps(False)
x

x = json.loads(x)
x

json.dumps(2)

json.dumps('hello')

json.dumps(2+3j)

json.dumps(None)

json.dumps({2,3,5,7})

json.dumps({2:'a', 3:'b'})

with open('data.json', 'w') as f:
    json.dump(x, f)

with open
