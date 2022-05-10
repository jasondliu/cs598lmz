import io
# Test io.RawIOBase
with io.BytesIO() as b:
    # Test io.BufferedIOBase
    with io.BufferedWriter(b) as bw:
        # Test io.TextIOBase
        with io.TextIOWrapper(bw, encoding='utf-8') as tw:
            tw.write('abc')
            assert tw.tell() == 3
            tw.seek(0)
