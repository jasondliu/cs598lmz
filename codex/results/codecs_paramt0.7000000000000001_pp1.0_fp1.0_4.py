import codecs
codecs.register_error('strict', codecs.ignore_errors)

#---------------------------------------------------------------------

def _pr_str(o):
    if isinstance(o, Number):
        return str(o)
    elif o is None:
        return "nil"
    elif o is True:
        return "true"
    elif o is False:
        return "false"
    elif isinstance(o, Symbol):
        return o.name
    elif isinstance(o, list):
        return "(" + " ".join(map(_pr_str, o)) + ")"
    elif isinstance(o, Vector):
        return "#(" + " ".join(map(_pr_str, o)) + ")"
    elif isinstance(o, Map):
        return "{" + " ".join(map(lambda x: _pr_str(x[0]) + " " + _pr_str(x[1]), o.items())) + "}"
    elif isinstance(o, str):
        return "\"" + o.replace("\\", "\\\\").replace("\"", "\\\"
