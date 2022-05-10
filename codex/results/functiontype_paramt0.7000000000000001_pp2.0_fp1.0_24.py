from types import FunctionType
list(FunctionType(lambda x: x+1, globals())(4))

# 14
class mylist(list):
    def __init__(self,*args):
        list.__init__(self,*args)
        self.sort()
    def append(self,value):
        list.append(self,value)
        self.sort()
    def insert(self,index,value):
        list.insert(self,index,value)
        self.sort()
    
print(mylist([1,2,3,4,5]))
print(mylist([5,4,3,2,1]))
print(mylist([1,3,2,4,5]))

# 15
class mydict(dict):
    def __init__(self,*args,**kwargs):
        dict.__init__(self,*args,**kwargs)
        
    def __setitem__(self,key,value):
        if key in self:
            raise ValueError('Exist key')
        else:
            dict.__setitem__(self,key
