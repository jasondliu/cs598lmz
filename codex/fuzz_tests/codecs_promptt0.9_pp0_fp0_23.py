import codecs
# Test codecs.register_error()
 
def schoenberg(exc): # The Schoenberg exception handler
    if isinstance(exc, UnicodeDecodeError):
        print(exc.start + 2)
        print(exc.end)
        print(exc.object)
        print(len(exc.object))
        print(exc.reason)
        print(exc.encoding)
        print(exc.start) 
       
        return (u"EuroSign", exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)
 
codecs.register_error(schoenberg)
 
print(str('\u20ac\u20ac\u20ac'.encode('ascii', 'schoenberg'), 'ascii'))

#_________________________Problem_1_______________________________________________________


def encode(astring):
    newstring = list(astring)
    ans = ''
    for x in newstring:
        ans += chr(ord(x)+1)
    return ans

def decode(astring):
    newstring =
