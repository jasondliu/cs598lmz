import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

app = Flask(__name__)
app.debug = True


def dbconnection(query):
    connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='sa', charset='utf8')
    cursor = connection.cursor()
    cursor.execute(query)
    if query.split()[0].lower() == 'select':
        connection.commit()
        result = cursor.fetchall()
    else:
        connection.commit()
        result = cursor.lastrowid
    cursor.close()
    connection.close()
    return result


def get_data(query):
    result = dbconnection(query)
    return result


def get_all(query):
    all_data = get_data(query)
    return all_data


def get_row(query):
    row_data = get_data(query)
    return row_data[0]


