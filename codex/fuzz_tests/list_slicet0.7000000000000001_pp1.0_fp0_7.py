import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

#
#       smart_str()
#
def smart_str(s, encoding='utf-8', errors='strict'):
    if not isinstance(s, basestring):
        try:
            return str(s)
        except UnicodeEncodeError:
            if isinstance(s, Exception):
                return ' '.join([smart_str(arg, encoding, errors) for arg in s])
            return unicode(s).encode(encoding, errors)
    elif isinstance(s, unicode):
        return s.encode(encoding, errors)
    elif s and encoding != 'utf-8':
        return s.decode('utf-8', errors).encode(encoding, errors)
    else:
        return s

#
#       create_unicode_buffer()
#
def create_unicode_buffer(size):
    buf = create_string_buffer(size * 2)
    return cast(buf, c_wchar_p)

#
#       resolve_unicode_buffer()
#
def resolve_unicode
