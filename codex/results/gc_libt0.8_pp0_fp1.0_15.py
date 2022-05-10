import gc, weakref
    #def __new__(cls, *args, **kwargs):
    #    self = super(SparseDict, cls).__new__(cls, *args, **kwargs)
    #    self.weak_refs = dict()
    #    return self
    
    def __init__(self):
        self.max_size = 2**32
        self.count = 0
        self.mapping = dict()
        
    def __contains__(self, item):
        return item in self.mapping.keys()
    
    def get_element(self, i):
        return self.mapping[i]
    
    def __getitem__(self, i):
        return self.get_element(i)
    
    def __setitem__(self, i, value):
        if not i in self.mapping:
            self.mapping[i] = value
            self.count += 1
            return
        if i in self.mapping:
            self.mapping[i] = value
    
#    def __
