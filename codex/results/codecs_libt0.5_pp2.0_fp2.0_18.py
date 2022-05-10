import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

with open('config.json', 'r') as f:
    config = json.load(f)

# TODO: move this to config
host = 'localhost'
port = 3306
user = 'root'
password = 'root'
db = 'tweet_sentiment'

try:
    conn = pymysql.connect(host, user=user, port=port, passwd=password, db=db, charset='utf8mb4')
except pymysql.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

cursor = conn.cursor()

cursor.execute("SET NAMES utf8mb4")
cursor.execute("SET CHARACTER SET utf8mb4")
cursor.execute("SET character_set_connection=utf8mb4")

def create_table():
    sql = "
