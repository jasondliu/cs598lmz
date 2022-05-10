from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct._FIELDS)
print s.__dict__

#from guppy.heapy import Remote
#import cPickle
#s = Remote(s)
#print cPickle.dumps(s)
