import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

g = open('utf-8.txt', 'rb')

b = g.read()

print(b)

p = b.decode('utf-8', errors='add_one_codepoint')
print(p)

q = p.encode('utf-16-le', errors='add_utf16_bytes')
print(q)

r = q.decode('utf-16-le', errors='add_one_codepoint')
print(r)

s = r.encode('utf-32-le', errors='add_utf32_bytes')
print(s)

t = s.decode('utf-32-le', errors='add_one_codepoint')
print(t)

u = t.encode('utf-8', errors='add_utf16_bytes')
print(u)

u.decode('utf-8', errors='strict')
