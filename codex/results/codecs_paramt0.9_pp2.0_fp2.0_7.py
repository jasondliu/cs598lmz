import codecs
codecs.register_error("strict", codecs.strict_errors)


class SmartOpen(object):
    """docstring for SmartOpen"""
    def __init__(self, *args, **kwargs):
        super(SmartOpen, self).__init__()
        self.fh = None
        self.filename = ''
        try:
            self.filename = args[0][0]
            self.fh = open(*args, **kwargs)
        except IOError:
            pass
        except TypeError, err_msg:
            pass

    def __del__(self):
        if self.fh:
            self.fh.close()

    def __getattr__(self, name):
        if self.fh:
            return getattr(self.fh, name)
        else:
            return None


class AppLogger(object):
    """docstring for AppLogger"""

    def __init__(self, appname='app'):
        super(AppLogger, self).__init__()

        if appname == 'app':
            appname = '
