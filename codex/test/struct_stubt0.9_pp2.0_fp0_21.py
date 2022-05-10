from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl',16)
s.size
'hhl'.encode('ascii')
size = Struct.size
size.__func__(s)
size(s)

# Pickling Instances

class mydata(object):
    def __init__(self,position_int,name=None):
        self.x = position_int
        self.y = None
        self.z = None
        self.name = None
        
m = mydata(23)

import pickle
with open('mydata.pkl','wb') as f:
    pickle.dump(m,f)

class mydata(object):
    def __init__(self,position_int,name=None):
        self.x = position_int
        self.y = None
        self.z = None
        self.name = None
        
    def __getstate__(self):
        d = dict(self.__dict__)
        d['version'] = 2
        return d
    
