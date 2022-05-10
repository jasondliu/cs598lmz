import codecs
codecs.register_error('ignore', codecs.ignore_errors)

reload(sys)
sys.setdefaultencoding('utf-8')

def processTime(timestr):
    timestr = timestr.replace("月", "-")
    timestr = timestr.replace("日", "")
    time = datetime.datetime.strptime(timestr, "%Y-%m-%d")
    return time

def processContent(content):
    content = content.replace('\r', '')
    content = content.replace('\n', '')
    content = content.replace('\t', '')
    content = content.replace(' ', '')
    content = content.replace('　', '')
    content = content.replace('|', '')
    return content

def process_special_character(content):
    content = content.replace('\n', '')
    content = content.replace('\t', '')
    content = content.replace('\r', '')
    content = content.replace(' ', '')
    content =
