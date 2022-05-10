import codecs
codecs.register(lambda name: Codec((
    CODEC_HELPERS.get(name),
    None,
    StreamReaderWriter(
        codecs.getreader('utf_8'), codecs.getwriter('utf_8'),
        codecs.getreader('utf_8_sig'), codecs.getwriter('utf_8_sig')))))
