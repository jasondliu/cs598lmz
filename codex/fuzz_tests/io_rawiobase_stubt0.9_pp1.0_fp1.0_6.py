import io
class File(io.RawIOBase):
    def __init__(self,node,filename,mode,buffering=-1):
        super().__init__()
        self._node = node
        
        if not (mode == "w" or mode == "wb"):
            raise OSError("Unsupported argument(s): {}".format(mode))

        self._w_open = True
        self._r_open = False
        self._filename = filename
        
    
    def __repr__(self):
        return "<{}: node:{} name:{}>".format(str(type(self)),str(self._node.id),self._filename)

    def write(self, b):
        n = node()
        n.writer = self._node
        n.parents.append(self._node)
        n["v"] = vb.VBytes(b)
        n.save()
    
    def writable(self):
        if self._w_open:
            return True
        else:
            return False 
    
    def seekable(self):
        return False

    def readable(self
