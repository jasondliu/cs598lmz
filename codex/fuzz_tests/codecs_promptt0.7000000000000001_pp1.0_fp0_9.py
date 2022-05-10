import codecs
# Test codecs.register_error('replace_with_space', ...)


def test_register_error():
    with pytest.raises(LookupError):
        codecs.lookup_error('replacewithspace')
    #
    codecs.register_error('replacewithspace', lambda e: (u' ', e.start+1))
    encoder, decoder, reader, writer = codecs.lookup_error('replacewithspace')
    assert isinstance(encoder, types.FunctionType)
    assert isinstance(decoder, types.FunctionType)
    assert isinstance(reader, types.FunctionType)
    assert isinstance(writer, types.FunctionType)
    #
    s = u'abc\u1234'
    assert codecs.encode(s, 'ascii', 'replacewithspace') == 'abc '.encode('ascii')
    assert codecs.decode(b'abc\xff', 'ascii', 'replacewithspace') == \
                                                     'abc\ufffd'.encode('ascii')
   
