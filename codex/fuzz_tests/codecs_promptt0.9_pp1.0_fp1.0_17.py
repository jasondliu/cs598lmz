import codecs
# Test codecs.register_error
def codec_name(input, errors='strict'):
    streamreader = codecs.getreader(unicode)(input, errors)
    test_string = u'string'
    for error in [
     'htmlcharrefreplace', 'ignore', 'htmldecode', 'replace', 'xmlcharrefreplace',
     'backslashreplace']:
        print "### " + error + " ###"
        streamreader = codecs.getreader(unicode)(input, errors)
        try:
            new_string = streamreader.read()
        except:
            new_string = u'exception'

        print repr(new_string), new_string


def codec_readline(input, errors='strict'):
    streamreader = codecs.getreader(unicode)(input, errors)
    print repr(streamreader.readline()), streamreader.readline()


class StreamReaderWriterTest1(unittest.TestCase):

    def test_error(self):
        input = StringIO('\xe4\xf6\xfc')
        codec_name
