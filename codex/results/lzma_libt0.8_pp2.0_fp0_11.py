import lzma
lzma.open
import pytest
import pdb

from lzma import LZMADecompressor

def get_testfiles():
    fn_files = glob.glob('testfiles/*.xz')
    return fn_files

def test_decompress_file():
    fn_files = get_testfiles()
    for fn in fn_files:
        assert decompress_file(fn) == open(fn.replace('.xz', ''), 'rb').read()

def test_extract_keyword():
    fn_files = get_testfiles()
    for fn in fn_files:
        decompressed_content = decompress_file(fn)
        assert extract_keyword(fn, decompressed_content) == '7Zip'
        
@pytest.mark.parametrize('fn,keyword', [
    ('testfiles/dummyAnal.cpp.xz', '7Zip'),
    ('testfiles/dummyAnal.cpp.xz', '7Zip'),
    ('testfiles/dummyAnal.cpp.x
