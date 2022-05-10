import codecs
codecs.register_error('strict', codecs.ignore_errors)

class ExceptionsProxy(object):

    def __init__(self, module):
        self.module = module

    def __getattr__(self, name):
        try:
            return getattr(self.module, name)
        except Exception, e:
            if not re.search('codec can\'t decode', str(e)):
                raise
            #print e
            return u''

sys.modules[__name__] = ExceptionsProxy(sys.modules[__name__])
