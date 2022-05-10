gi = (i for i in ())
# Test gi.gi_code.co_flags for the flag
# defining whether the generator is
# currently executing.
#
# Python 3.5.2
CUSTOM_GEN_FLAG = 64

class MultiMapping(dict):
    def getlist(self, key, type=None): # pragma: no cover
        v = self[key]
        if type is not None:
            v = type(v)
        if isinstance(v, (list, tuple)):
            return v
        elif v is None:
            return ()
        return [v]

    def mixed(self): # pragma: no cover
        """Returns a list like [(k, v), ...] where mappings
        with multiple values for a key result in multiple
        items.  This is useful to construct query strings or
        POST data.
        """
        rv = []
        for key, value in iteritems(self):
            rv.extend((key, x) for x in self.getlist(key, type=to_native))
        return rv

    def items(self, multi=False): # pragma
