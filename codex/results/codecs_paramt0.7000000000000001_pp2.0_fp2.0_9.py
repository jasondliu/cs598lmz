import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Zone(object):
    """An Rdata Zone"""
    def __init__(self, rdata):
        self.rdata = rdata
        self.name = rdata[0].name
        self.data = rdata[1]

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self.name)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Record(object):
    """An Rdata Record"""
    def __init__(self, rdata):
        self.rdata = rdata
        self.name = rdata[0].name
        self.data = rdata[1]

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self.name)

    def __str__(self):
        return self.name

    def __unic
