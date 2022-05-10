import _struct as struct

def _vsnprintf(buf, length, format, ap):
    return _vsnprintf_s(buf, length, length, format, ap)
    
def _snprintf(buf, length, format, ...):
    return _snprintf_s(buf, length, length, format, __va_args__)

def __streq(x, y):
    return x == y

def __strneq(x, y, n):
    return x == y

def _mbscmp(x, y):
    return x == y

def _mbscmpi(x, y):
    return x == y

def _mbsicmp(x, y):
    return x == y

def _mbsicmp_l(x, y):
    return x == y

def _mbsnbicmp(x, y):
    return x == y

def _mbsnbicmp_l(x, y):
    return x == y

def _mbsnbcmp(x, y):
    return x == y


