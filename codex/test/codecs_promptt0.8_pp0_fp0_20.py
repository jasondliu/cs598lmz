import codecs
# Test codecs.register_error


def err(codec_name):
    """Make a one-off error handler that raises a UnicodeError."""
    def handler(exception):
        return ('', exception.start + 1)
    return handler


