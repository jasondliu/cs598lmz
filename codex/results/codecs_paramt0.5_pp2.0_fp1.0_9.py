import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

#configuration
CONFIG_FILE = 'config.ini'

#logging
LOG_FILE = 'log.txt'
LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
LOG_LEVEL = logging.INFO

#get config
config = configparser.ConfigParser()
config.read(CONFIG_FILE)

#set logging
logging.basicConfig(filename=LOG_FILE, format=LOG_FORMAT, level=LOG_LEVEL)

#get config values
DB_USER = config['database']['user']
DB_PASSWORD = config['database']['password']
DB_HOST = config['database']['host']
DB_NAME = config['database']['name']
DB_TABLE = config['database']['table']

#connect to database
db = MySQLdb.connect(user=DB_USER, passwd=DB_PASSWORD, host=DB_HOST, db=DB_NAME)

