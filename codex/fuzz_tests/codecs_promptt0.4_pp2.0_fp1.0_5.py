import codecs
# Test codecs.register_error
import encodings.utf_8

def test_main():
    # Test codecs.register_error
    def my_handler(exception):
        return ("", exception.end)
    codecs.register_error("test.my_handler", my_handler)
    assert codecs.lookup_error("test.my_handler") is my_handler
    assert codecs.lookup_error("test.my_handler2") is None
    # Test codecs.register
    def my_encoder(obj):
        return "", ()
    def my_decoder(obj):
        return "", ()
    def my_stream_reader(stream):
        return codecs.StreamReader(stream, my_decoder, my_stream_reader)
    def my_stream_writer(stream):
        return codecs.StreamWriter(stream, my_encoder, my_stream_writer)
    codecs.register(my_encoder, my_decoder, my_stream_reader, my_stream_writer)
    assert codecs.lookup("test.my_encoder
