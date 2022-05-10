import lzma
lzma = lzma
from data_structures import p20

def test_parse_with_nulls():
    s = b'pip\x00etre\x00'
    assert parse_names(s) == ['pip', 'etre']


def test_parse01():
    result = parse_names(b"pip\x00")
    assert result == ["pip"]


def test_parse02():
    result = parse_names(b"pip\x00etre\x00")
    assert result == ["pip", "etre"]


def test_parse03():
    result = parse_names(b"pip\x00etre\x00chat\x00")
    assert result == ["pip", "etre", "chat"]


def test_parse_with_compressed_data():
    s = b'pip\x00etre\x00chat\x00'
    s = lzma.compress(s)
    assert parse_names(s) == ['pip', 'etre', 'chat']


