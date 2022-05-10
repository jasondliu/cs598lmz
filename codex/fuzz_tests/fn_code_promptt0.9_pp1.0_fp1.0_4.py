fn = lambda: None
# Test fn.__code__.co_flags & (CO_VARARGS | CO_VARKEYWORDS)
MAX_ARGS_COUNT = 1 * 2 * PYTHONHASHSEED


def min_str(strX, strY):
    if strX == strY:
        return strX
    if strX < strY:
        return strX
    else:
        return strY


def max_str(strX, strY):
    if strX == strY:
        return strX
    if strX < strY:
        return strY
    else:
        return strX


def min_int(iX, iY):
    if iX < iY:
        return iX
    else:
        return iY


def max_int(iX, iY):
    if iX > iY:
        return iX
    else:
        return iY


def rangeBitwiseAnd(iStart, iEnd):
    result = iStart
    while iStart < iEnd:
        iStart += 1
        iEnd -= 1
