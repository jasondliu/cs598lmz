import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Set the default encoding to utf-8
# This is not a "correct" solution. But it works!
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Set the logging level
logging.basicConfig(level=logging.INFO)

# Set the number of threads
thread_count = 4

# Set the default timeout
timeout = 10

# Set the default user agent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

# Set the default headers
headers = {
    'User-Agent': user_agent,
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Accept-Encoding': 'g
