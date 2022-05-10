import codecs
codecs.register_error('strict', codecs.ignore_errors)
import sys

def _getUnicode(value, encoding='utf-8', noneToNull=False):
    if noneToNull and value is None:
        return None
    if not isinstance(value, unicode):
        value = unicode(str(value), encoding, 'strict')
    return value

def _getStr(value, encoding='utf-8', noneToNull=False):
    if noneToNull and value is None:
        return None
    if not isinstance(value, basestring):
        value = str(value)
    if isinstance(value, unicode):
        value = value.encode(encoding)
    return value

def _getInt(value, noneToNull=False):
    if noneToNull and value is None:
        return None
    return int(value)

def _getFloat(value, noneToNull=False):
    if noneToNull and value is None:
        return None
    return float(value)

def _getTolerance(value, noneToNull
