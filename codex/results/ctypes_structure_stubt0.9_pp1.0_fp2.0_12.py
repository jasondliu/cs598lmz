import ctypes

class S(ctypes.Structure):
    x = ctypes.c_byte(12)

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '_asdict'): # Structures
            return obj._asdict()
        elif isinstance(obj, (list, tuple)): # Lists and tuples
            return [self.default(e) for e in obj]
        elif isinstance(obj, (dict, OrderedDict)): # Dictionaries and OrderedDicts
            d = OrderedDict()
            for key, value in obj.items():
                d[key] = self.default(value)
            return d
        elif isinstance(obj, uuid.UUID): # UUIDs
            return str(obj)
        elif isinstance(obj, ctypes.c_byte): # ctypes are somehow arrays?
            return obj.value
        else:
            return super(MyEncoder, self).default(obj)

s = S()

struct = {
    "test": s,
    "tuple": (s
