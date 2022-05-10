import bz2
bz2.VERSION

# pickle module
# dumps(obj) - Returns a string containing the pickled obj
# load(file) - Returns a python obj equivalent to the pickled data in file
pickle.dumps([1,2,3])
tab = [1,2,{'key1':'value1', 'key2': 'value2'}]
pickledStr = pickle.dumps(tab)
tab2 = pickle.loads(pickledStr)
tab2 == tab
# we can use this module to send binary data and retrieve it from network

# in python3 we can do
import json
json.dumps([1,2,'1',[1, 2, True]])
json.dumps({'4':5, '6':7, 8: 9,10:11})
json.loads('{"4": 5, "6": 7, "8": 9, "10": 11}')

# JSON for humans
import pprint
t = json.loads('{"4": 5, "6": 7, "8": 9, "10": 11}')
pprint.pprint
