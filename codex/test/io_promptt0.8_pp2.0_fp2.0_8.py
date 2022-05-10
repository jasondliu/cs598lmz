import io
# Test io.RawIOBase.readinto()
def test_io_RawIOBase_readinto(benchmark):
    def test_data():
        for i in range(1, 10):
            for j in range(1, i*1000):
                f = io.BytesIO()
                f.seek(0, io.SEEK_END)
                f.write(b'\x00'*i*1000)
                f.seek(0)
                data = bytearray(i*1000)
                benchmark(f.readinto, data)
    test_data()

# Test io.RawIOBase.readinto1()
def test_io_RawIOBase_readinto1(benchmark):
    def test_data():
        for i in range(1, 10):
            for j in range(1, i*1000):
                f = io.BytesIO()
                f.seek(0, io.SEEK_END)
                f.write(b'\x00'*i*1000)
                f.seek(0)
                data = bytearray(i*1000)

