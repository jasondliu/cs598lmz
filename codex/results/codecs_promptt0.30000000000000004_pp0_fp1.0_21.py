import codecs
# Test codecs.register_error

def my_errorhandler(exception):
    print("my_errorhandler called")
    return (u'', exception.end)

codecs.register_error("test.my_errorhandler", my_errorhandler)

def my_errorhandler_factory(name):
    print("my_errorhandler_factory called")
    return my_errorhandler

codecs.register_error("test.my_errorhandler_factory", my_errorhandler_factory)

def my_errorhandler_tuple(exception):
    print("my_errorhandler_tuple called")
    return (u'', exception.end)

codecs.register_error("test.my_errorhandler_tuple", (my_errorhandler_tuple,
                                                     my_errorhandler_tuple))

def my_errorhandler_dict(exception):
    print("my_errorhandler_dict called")
    return (u'', exception.end)

codecs.register_error("test.my_errorhandler_dict", {'xmlcharrefreplace
