import io
# Test io.RawIOBase
assert issubclass(io.RawIOBase, io.IOBase)
# help(io.RawIOBase)

# Test io.TextIOBase
assert issubclass(io.TextIOBase, io.IOBase)
# help(io.TextIOBase)

# TextIOBaseとRawIOBaseで同じメソッドがあるという擬似静的契約
for base_class in io.TextIOBase, io.RawIOBase:
    # TODO: あとで確認
    for x in [
            'read', 'readinto', 'readline', 'readlines',
            # 'write',
            'seek', 'seekable', 'tell', 'truncate', 'readable',
            # 'writable', 'flush', 'close', 'isatty', 'closed'
            ]:
        assert hasattr(base_class, x), x


# RawIOBaseのサブクラス内でseek()をサポートする例
class BytesIOW
