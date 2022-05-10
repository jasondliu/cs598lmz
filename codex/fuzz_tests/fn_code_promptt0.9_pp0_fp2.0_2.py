fn = lambda: None
# Test fn.__code__ to see whether fn is a no-op
nop_test = (callable(fn) and any("dummy" in kw for kw in fn.__code__.co_varnames))
PROJ_LIB = os.environ.get('PROJ_LIB', nop_test)
PROJ_LIB = env.str('PROJ_LIB', nop_test)
del env

if not PROJ_LIB:  # set and tested in __init__.py
    raise EnvironmentError("PROJ_LIB environment variable not set")
try:
    os.environ['PROJ_LIB'] = PROJ_LIB
    from _proj import Proj, _proj
except ImportError as err:
    raise ImportError("%s - %s" % (err,
                      "please check that PROJ_LIB points to a valid directory"))

MAX_ITER = 4  # this is large because fwd invs can oscillate in some zones
R_MAJOR = _proj.PJ_ELLIPSES["WGS 84"][0]
R_MINOR = _
