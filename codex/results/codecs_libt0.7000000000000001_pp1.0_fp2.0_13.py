import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Constants
_MAX_RETRY = 3
_MAX_PAGE_NUM = 5
_TIMEOUT = 30
_MAX_PRODUCT_NUM = 5
_SAVE_RESULT_DIR = './result/'
_SAVE_LOG_DIR = './log/'
_LOG_FILENAME = 'log-%s.txt' % datetime.datetime.now().strftime('%Y-%m-%d')
_LOG_ENCODING = 'utf-8'
_LOG_FORMAT = '%(asctime)s: %(levelname)s: %(message)s'
_LOG_FORMATTER = logging.Formatter(_LOG_FORMAT)
_USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    '
