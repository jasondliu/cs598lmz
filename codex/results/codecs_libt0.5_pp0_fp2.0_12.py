import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# import config
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# connect to mysql
conn = pymysql.connect(host=config['mysql']['host'],
                       user=config['mysql']['user'],
                       password=config['mysql']['password'],
                       db=config['mysql']['db'],
                       charset='utf8mb4')
cursor = conn.cursor()

# connect to mongodb
client = MongoClient(config['mongo']['host'], int(config['mongo']['port']))
db = client[config['mongo']['db']]
collection = db[config['mongo']['collection']]

# get user_ids
cursor.execute('select distinct user_id from users')
user_ids = [row[0] for row in cursor.fetchall()]

# get
