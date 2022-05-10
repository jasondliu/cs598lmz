import bz2
bz2.open(fname)
'''

'''
#11 gzip
import gzip
gzip.open(fname)
'''
'''
#12 copy
import copy
copy.copy(data)
copy.deepcopy(data)
'''
'''
a=1
b=a
a=2
a
b
'''
'''
class Bus:
    def __init__(self,passengers=None):
        if passengers is None:
            self.passengers=[]
        else:
            self.passengers=list(passengers)
    def pick(self,name):
        self.passengers.append(name)
    def drop(self,name):
        self.passengers.remove(name)

import copy
bus1=Bus(['Alice','Bill','Claire','David'])
bus2=copy.copy(bus1)
bus3=copy.deepcopy(bus1)
bus1.drop('Bill')
bus2.passengers
bus3.passengers
'''
'''
#13 
import shelve

