import gc, weakref

class V:
    """This class is a placeholder for a variable"""
    pass
        
class MyGraph():
    def __init__(self,g=None):
        if g is None: 
            self.g=[]
        else:
            self.g = g
        

    def edge(self, dest, src):
        #self.g.setdefault(dest, []).append(src) 
        if dest not in self.g:
            self.g.append(dest)
        if dest not in src.list_of_justs:
            src.list_of_justs.append(dest)
        
    def way(self, src):
        seen=[]
        next=[]
        next.append(src)
        while next:
            cur=next.pop(0)
            for new in cur.list_of_justs:
                if new not in seen:
                    next.append(new)
            seen.append(cur)
        return seen
        #return set(src.list_of_justs)
 
    def pr
