import codecs
codecs.register_error('copy_error', codecs.ignore_errors)

class _ContentHandler(object):
    def __init__(self, writer):
        self.writer = writer

    def handle(self, match):
        if self.writer.closed:
            raise ValueError('File is closed!')
        content = match.group('content')
        if content:
            self.writer.write(content)


# TODO: set the error handler to 'copy_error' on the codecs
class _IgnoreEncodingHandler(_ContentHandler):
    def handle(self, match):
        if self.writer.closed:
            raise ValueError('File is closed!')
        tag = match.group('tag')
        content = match.group('content')
        if tag is None:
            if content:
                self.writer.write(content)
        elif tag == '<?':
            pass
        elif tag == '<!':
            pass
        elif tag == '<![':
            pass
        elif tag == '</':
            pass
        elif tag == '<
