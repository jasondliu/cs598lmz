import bz2
# Test BZ2Decompressor is required because BZ2Decompressor is not defined in Python 2.6
try:
    BZ2Decompressor()
except:
    raise Exception('BZ2Decompressor() is not defined, please use Python 2.7 or newer')

# Simple test for the tardis.io.util module

def test_bz2_reader():
    test_data = bz2.compress('test input')
    test_file = StringIO.StringIO(test_data)
    with BZ2FileReader(test_file) as reader:
        data = reader.read()
    assert data == 'test input'

def test_bz2_writer():
    test_file = StringIO.StringIO()
    with BZ2FileWriter(test_file) as writer:
        writer.write('test input')
        writer.write('test input')
        writer.flush()
    test_data = test_file.getvalue()
    assert test_data == bz2.compress('test input') + bz2.compress('test input')
