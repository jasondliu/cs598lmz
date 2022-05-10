import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Plugin(Base):
    __name__ = 'podcatcher'
    __type__ = 'storage'
    __version__ = '0.7'
    __status__ = 'stable'

    __pattern__ = r'http://(?:www\.)?podcatcher\.de/.*(?P<TYPE>track)/.*'
    __config__  = [("use_premium", "bool", "Use premium account if available", True)]

    __description__ = """podcatcher.de storage plugin"""
    __license__     = "GPLv3"
    __authors__     = [("blackglory", "")]

    def setup(self):
        self.multiDL = self.premium
