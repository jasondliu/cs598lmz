import _struct

# type code for Python's built-in types
structcode = {}

def compute_structcode():
    for name in dir(_struct):
        if name.startswith('__'):
            continue
        type, _, _ = _struct.__getattribute__(_struct, name)
        structcode.setdefault(type, {})
        structcode[type][name] = _struct.__getattribute__(_struct, name)

compute_structcode()

codes = structcode.keys()
codes.sort()

for code in codes:
    print '%3d: %s' % (code, structcode[code].keys())
