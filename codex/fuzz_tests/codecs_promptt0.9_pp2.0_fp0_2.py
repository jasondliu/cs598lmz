import codecs
# Test codecs.register_error for error handler for unknown encoding
import encodings.iso8859_16
import encodings.shift_jis

with codecs.lookup('iso8859_16') as codec:
    assert codec.name == 'iso8859_16'
    with pytest.raises(ValueError):
        codecs.lookup('iso8859_16')
with codecs.lookup('shift_jis') as codec:
    assert codec.name == 'shift_jis'
    with pytest.raises(ValueError):
        codecs.lookup('shift_jis')


def test_handler_for_unknown_code(monkeypatch):
    def handler_for_unknown(ex):
        raise RuntimeError("xyz")
    monkeypatch.setattr(codecs, "handler_for_unknown", handler_for_unknown)
    with pytest.raises(RuntimeError) as excinfo:
        codecs.encode("\xff", "xyz")
    assert str(excinfo.value) == "xyz"


# tests for encodings that
