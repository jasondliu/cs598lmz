import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# set up sqlite db
sqlite_db = SQLITE_DB

# set up mysql db
#mysql_db = MYSQL_DB

# set up logging
# set format and log level
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_LEVEL = "DEBUG"
# set log file path and name
LOG_FILE_PATH = './log/'
LOG_FILE_NAME = 'imdb_user_info_crawl.log'

# set chromedriver path
CHROME_DRIVER_PATH = r'C:\chromedriver_win32\chromedriver.exe'

# set imdb user url
IMDB_USER_URL = "https://www.imdb.com/user/ur{user_id}"

# set headers
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) Apple
