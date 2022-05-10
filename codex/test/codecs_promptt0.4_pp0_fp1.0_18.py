import codecs
# Test codecs.register_error
def my_ignore_error(exception):
    print("Ignoring", exception)
    return (u'', exception.end)
codecs.register_error("ignore", my_ignore_error)
