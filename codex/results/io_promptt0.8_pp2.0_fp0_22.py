import io
# Test io.RawIOBase
s = io.StringIO("file: \n\t\b  \r\v\f\a\0\1\2\3\4\5\6\7\8\9\x1b\x09 \t")
s.seek(0)
print(s.readline())
