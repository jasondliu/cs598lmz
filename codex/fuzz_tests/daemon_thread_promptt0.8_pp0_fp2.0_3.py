import threading
# Test threading daemon
# See http://stackoverflow.com/questions/19334066/get-all-key-values-from-a-python-dict
def check_dict(d):
    for k in d.keys():
        if type(d[k]) is dict:
            return True
    return False

def flatten_dict(d):
    stack = [((), d)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if isinstance(v, dict):
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    return result

# Test if dict is empty
def is_empty(d):
    if not d:
        return True
    if type(d) is dict:
        return len(d) == 0
    else:
        return False

# Returns a dict containing the features and their types (len,type)
def get_features(data):
    features = {}
    for
