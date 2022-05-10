import _struct as struct

def _vsnprintf(buf, length, format, ap):
    return _vsnprintf_s(buf, length, length, format, ap)
    
