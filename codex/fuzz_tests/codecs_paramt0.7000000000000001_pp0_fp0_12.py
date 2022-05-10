import codecs
codecs.register_error('surrogate_or_special',
                      lambda e: (u'�', e.start + 1))
codecs.register_error('surrogate_or_special_ignore',
                      lambda e: (u'', e.start + 1))

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
         if isinstance(o, ObjectId):
             return str(o)
         else:
             return json.JSONEncoder.default(self, o)
class Dict(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

def toDict(d):
    D = Dict()
    for k, v in d.iteritems():
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D
def
