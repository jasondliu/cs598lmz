import bz2
bz2.BZ2File(filename)

import gzip
gzip.open(filename,'rt')

import lzma
lzma.open(filename)

#14.4.4 Pickle
import pickle
pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pkl_file.close()

with open('data.pkl', 'rb') as pkl_file:
    data2 = pickle.load(pkl_file)

data1 == data2

#14.4.5 Shelve
import shelve
s = shelve.open('test.dat')
s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
s['key1']

s.close()

s = shelve.open('test.dat')
list(s.keys())

list(s.values())

s.close()

s = shelve.open('test.dat',writeback=True)
s['key1'
