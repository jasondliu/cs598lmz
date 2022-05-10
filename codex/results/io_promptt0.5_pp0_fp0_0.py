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
            assert tw.read(1) == 'a'
            tw.seek(0, io.SEEK_END)
            assert tw.tell() == 3
            tw.write('d')
            assert tw.tell() == 4
            tw.seek(0)
            assert tw.read() == 'abcd'
            tw.seek(0)
            assert tw.read(5) == 'abcd'
            tw.seek(0)
            assert tw.read(-1) == 'abcd'
            tw.seek(0)
            assert tw.readline() == 'abcd'
            tw.seek(0)
            assert tw.readline(2) == 'ab'
           
