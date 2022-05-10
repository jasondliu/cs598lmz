import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='pacman_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def get_scores():
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `name`, `score` FROM `score` ORDER BY `score` DESC LIMIT 10"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def add_score(name, score):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `score` (`name`, `score`) VALUES (%s, %s)"
            cursor
