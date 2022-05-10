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

for name in dir(codecs):
    if name.endswith("_encode"):
        x = getattr(codecs, name)
        setattr(codecs, name, lambda text, errors="strict": x(text, "add_one_codepoint"))

for name in dir(codecs):
    if name.endswith("_encode"):
        x = getattr(codecs, name)
        setattr(codecs, name, lambda text, errors="strict": x(text, "add_utf16_bytes"))

for name in dir(codecs):
    if name.endswith("_encode"):
        x = getattr(codecs, name)
        setattr(codecs, name, lambda text, errors="strict": x(text, "add_utf32_bytes"))
```

在Python 3.x中：

```
a = bytes([230, 136, 145])
```

得到的字符串
