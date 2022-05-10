import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_int, ctypes.c_int)
## EXPORT: line_diff --
# CALC_FUNC = FUNTYPE(c.line_diff)
CALC_FUNC = FUNTYPE(c.line_difference)

## EXPORT: line_num
def line_num(f):
    """convert to netcdf line number"""
    nuv = yaml.load(f.read())
    f.seek(0)
    i = 0
    for l in f:
        _n = CALC_FUNC(nuv[i], i)
        if _n:
            yield l, i+_n
        i += 1
##

## EXPORT: append_line_num
def append_line_num(fname):
    with open(fname) as f:
        for l, i in line_num(f):
            yield "%3d: %s" % (i, l)
##

## EXPORT: main
def main(*fnames):
    if fnames:
        for
