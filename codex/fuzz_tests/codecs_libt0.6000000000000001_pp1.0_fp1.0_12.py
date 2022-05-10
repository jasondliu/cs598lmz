import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# connect to the MySQL server
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='sakila',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def run(sql):
    """ Helper function to run SQL statements """
    with connection.cursor() as cursor:
        cursor.execute(sql)
    return cursor.lastrowid


def add_actor(first_name, last_name):
    sql = "INSERT INTO actor (first_name, last_name) VALUES (%s, %s);"
    data = (first_name, last_name)
    return run(sql, data)


def add_address(address, district, city_id):
    sql = "INSERT INTO address (address, district, city_id) VALUES (%s, %s, %s);
