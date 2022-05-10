from types import FunctionType
list(FunctionType(a.func_code, {}, None, None, a.func_defaults))

# TODO: proper tests
#d = dict()
#d.update(a.func_defaults)
#a.func_defaults.keys()
#a.func_defaults.values()
#a.func_defaults.items()
#d.keys()
#d.values()
#d.items()
#
#[k for k in d if d[k] is not get_param_default(a)]
#[k for k in d if d[k] is get_param_default(a)]
#
#{k: d[k] for k in d if d[k] is not get_param_default(a)}
#{k: d[k] for k in d if d[k] is get_param_default(a)}
#
#{k: d[k] for k in a.func_code.co_varnames if d[k] is not get_param_default(a)}
#{k: d[k] for k in a.
