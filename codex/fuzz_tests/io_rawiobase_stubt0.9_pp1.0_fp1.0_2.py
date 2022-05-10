import io
class File(io.RawIOBase):
    """Wrapper for data coming from an opened file"""
    
    def __init__(self, source=None):
        self._data = source
        self._input_file = None
        self._opened = None
        self._is_summary_ready = False
        if self._data is not None:
            self.open(source)
            
    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result
        
    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))
        return result
        
    def __del__(self):
        if self._opened:
            self.close()
        
    def __len__(self):

