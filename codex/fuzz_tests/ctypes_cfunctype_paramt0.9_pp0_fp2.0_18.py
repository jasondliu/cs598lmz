import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
class Annotatorcallbacks(ctypes.Structure):
    _fields_ = [("get", FUNTYPE), ("set", FUNTYPE), ("seti", FUNTYPE), ("setx", FUNTYPE), ("setxxi", FUNTYPE)]

# libxml2 initialization
try:
    libxml2.initParser()
except:
    pass

_GRP_CHAR = '[^\\\\,]'
_RX_GROUP = r'\\,' # Match escaped comma
_RX_DOUBLE_QUOTE = r'\\\\"'
_RX_DOUBLE_ESCAPES = r'\\\\'
_RX_DOUBLE_QUOTE_OR_ESCAPES = r'\\\\|\\"'
_RX_DOUBLE_QUOTE_OR_COMMA = r'\\,|\\\\"|\\"'
_RX_STRING = r"\"(?P<str>%s*?)\"" % _RX_DOUBLE_QUOTE
_RX_STRINGLIST_QUOTE = r
