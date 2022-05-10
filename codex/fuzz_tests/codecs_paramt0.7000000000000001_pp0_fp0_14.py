import codecs
codecs.register_error('strict', codecs.ignore_errors)

sys.path.append(os.path.abspath('../Common'))
import CommonUtils

# -----------------------------------------------------------------------------
#  Class
# -----------------------------------------------------------------------------
class Document():
    def __init__(self, filePath):
        self.filePath = filePath
        self.docElem = None
        self.encoding = None

    def parse(self):
        self.__detectEncoding()
        self.__parse()

    def __detectEncoding(self):
        self.encoding = CommonUtils.detectFileEncoding(self.filePath)

    def __parse(self):
        try:
            self.docElem = ET.parse(self.filePath, ET.XMLParser(encoding=self.encoding))
        except UnicodeDecodeError:
            print('[Error] Cannot parse {0}'.format(self.filePath))
