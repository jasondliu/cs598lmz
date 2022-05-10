import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import pymysql


host = "127.0.0.1"
user = "root"
password = ''
dbname = "stock"
charset = "utf8mb4"

def main():
    connection = pymysql.connect(host=host, user=user, password=password, db=dbname, charset=charset,
                                 cursorclass=pymysql.cursors.DictCursor)

    return connection


def get_csrc_items(connection, limit=10000):
    cursor = connection.cursor()
    sql = "SELECT * from csrc_items as a LEFT JOIN csrc_stock_report as b on a.stock_code=b.stock_code limit 1"
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


def get_csrc_stock(connection, limit=10000):
    cursor = connection.cursor()
    sql =
