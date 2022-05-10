import io
class File(io.RawIOBase):
    """
    A kino file with multiple chunks, cross-references and an LUT
    """
    def __init__(self,name,*args,**kwargs):
        self.chunks = OrderedDict()
        self.name = name
        self.lut = None
        #self.xrefs = {} 
        
        self.setpos(0)
        self.size = 0

    def getpos(self):
        pos = 0
        for x in self.chunks:
            pos += self.chunks[x].getpos()
        return pos

    def setpos(self,pos):
        passed = 0
        self.getchunk = None
        self.getmode = None
        for x in self.chunks:
            chunk = self.chunks[x] 
            size = chunk.getsize()
            if pos > passed + size:
                passed += size
            else:
                self.getchunk = x
                self.getmode = 'setpos'
                chunk.setpos(pos - passed)
                break

       
