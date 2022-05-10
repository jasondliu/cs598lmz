import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# establish database connection
db_connection = pymysql.connect(host=os.getenv('MYSQL_HOST'),
                             user=os.getenv('MYSQL_USER'),
                             password=os.getenv('MYSQL_PASSWORD'),
                             db='itm',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def get_all_university_names():
    try:
        with db_connection.cursor() as cursor:
            cursor.execute("SELECT University_Name FROM university")
            result = cursor.fetchall()
            return result
    except Exception as ex:
        return (ex)


def insert_university(university_name, university_url):
    try:
        with db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO university (University_Name,University_URL) VAL
