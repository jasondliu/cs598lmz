import ctypes
ctypes.cast(0, ctypes.py_object).value = 'abc'
s[0]

s = Series()
s[0] = 'hello'
s

len(s)

# Creating a Series using Python dict
data = {'Ohio': 35000, 'Oregon': 16000, 'Texas': 71000, 'Utah': 5000}
s = Series(data)
s

# If a Series is created from a dict, the Series index will be the keys from the dict
states = ['California', 'Ohio', 'Oregon', 'Texas']
s = Series(data, index=states)
s

s.isnull()

s.notnull()

s[s.notnull()]

s.name = 'population'
s.index.name = 'state'
s

# Series objects can be modified inplace
s['California'] = 1400000
s

# Series object can also be treated like a fixed-size dict
s['California']

# Example:
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
       '
