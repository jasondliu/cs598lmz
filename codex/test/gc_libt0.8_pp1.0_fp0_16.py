import gc, weakref, time


def remove_from_dict(d, key):
    if not isinstance(d, dict):
        return

    if key in d:
        del d[key]

    for item in d.values():
        remove_from_dict(item, key)


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


def get_class(kls):
    """
    This function should be used when you are using modules that are not directly known to the system
    and you cannot import them, e.g. if you want to pass a module name as a parameter
    """
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m


