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

def test_main():
    # Test UTF-8
    for s in ["\u20ac", "\u20ac\u20ac", "\u20ac\u20ac\u20ac"]:
        for i in range(len(s)):
            for j in range(i, len(s)):
                for k in range(j, len(s)):
                    for l in range(k, len(s)):
                        for m in range(l, len(s)):
                            for n in range(m, len(s)):
                                for o in range(n, len(s)):
                                    for p in range(o, len(s)):
                                        for q in range(p, len(s)):
                                            for r in range(q, len(s)):
                                                for s in range(r, len(s)):
                                                    for t in range(s, len(s)):
                                                        for u in range(t, len(s)):
                                                            for v in range(u, len(s
