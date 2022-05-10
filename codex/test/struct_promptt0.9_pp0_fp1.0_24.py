import _struct
# Test _struct.Struct('a')
def _get_size_and_alignment(s):
    return _struct.calcsize(s), _struct.Struct(s).align
class _SimpleCDataMeta(type(cdata)):

    def __new__(self, name, *args, **kwargs):
        final_fields = kwargs.pop('final_fields', ())
        res = super(_SimpleCDataMeta, self).__new__(self, name, *args, **kwargs)
        res.final_fields = final_fields
        return res

    def _become_final_type(self):
        """Replace cls by the type that contains all final fields
        """
        if self.final_fields == ():
            return self, ()
        bases = [getattr(self, f) for f in self.final_fields]
        realbases = _uniq([t._become_final_type()[0] for t in bases])
        if realbases == (self,):
            return self, ()
        newfields = {}
        conv = []
