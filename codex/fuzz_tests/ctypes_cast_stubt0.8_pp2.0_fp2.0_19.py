import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

def _dump(obj, depth=0, max_depth=10):
    if depth > max_depth:
        return str(type(obj))

    result = []

    if isinstance(obj, dict):
        result.append('{')
        result += [_dump(k, depth + 1, max_depth) + ': ' + _dump(v, depth + 1, max_depth) + ',\n'
                   for k, v in obj.items()]
        result.append('}')
    elif isinstance(obj, list):
        result.append('[')
        result += [_dump(k, depth + 1, max_depth) + ',\n' for k in obj]
        result.append(']')
    else:
        result.append(repr(obj))

    res = ''.join(result)
    if len(res) < 10000:
        return res
    else:
        return res[:10000] + '...'

print _dump(caller.f_glob
