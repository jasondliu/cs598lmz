import codecs
codecs.register_error('strict', codecs.ignore_errors)

class ConfigParser(RawConfigParser):

    def __init__(self, defaults=None):
        RawConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

    def read(self, filenames):
        if isinstance(filenames, basestring):
            filenames = [filenames]
        read_ok = []
        for filename in filenames:
            try:
                fp = open(filename)
            except IOError:
                continue
            self._read(fp, filename)
            fp.close()
            read_ok.append(filename)
        return read_ok

    def get(self, section, option, raw=False, vars=None):
        return RawConfigParser.get(self, section, option, raw, vars)

    def items(self, section, raw=False, vars=None):
        return RawConfigParser.items(self, section, raw, vars)

    def getint
