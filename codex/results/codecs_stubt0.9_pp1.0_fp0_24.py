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

def decorator(dec):
    class Foo:
        @dec
        def my_function(self):
            return 42
    return Foo().my_function

class Foo:
    def bar(self):
        def f():
            pass

        return f

    def baz(self):
        return lambda: None

def test():
    a = [15] * 16
    b = [None] * 16
    c = ''
    d = {a[i]: i for i in range(16)}
    e = 42

    a.append(e)
    yield from a

    b += a
    b[1:] = a

    c += 'Hello!'

    def deep():
        a.append(e)
        yield from a

        b += a
        b[1:] = a

        c += 'Hello!'

        for i in a:
            for j in b:
                for k in c:
                    yield from a
                    yield from b
                    yield from c

                    a.append(e)
                    b += a
                    b[1:] = a

