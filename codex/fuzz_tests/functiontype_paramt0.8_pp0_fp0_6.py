from types import FunctionType
list(FunctionType('foo'))

def to_list(x):
    return list(x) if type(x) in (RangeType, TupleType, ListType) else [x]
    
    
def to_dict(d):
    D = {}
    for k,v in d:
        if type(k) in (ListType, RangeType):
            for x in k: D[x] = v
        else: D[k] = v
    return D

class MyDict(dict):
    def __init__(self, d={}):
        if type(d) is dict: dict.__init__(self, d)
        else: dict.__init__(self,  to_dict(d))
    def __getitem__(self, key):
        try: res = dict.__getitem__(self, key)
        except: res = dict.__getitem__(self, 0)
        return res

def add(x,y): return x + y

def accumulate(seq, fun=add): 
    it = iter(seq)
    total
