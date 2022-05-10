import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


class MySQL2(object):
    def __init__(self, host, username, passwd, db_name, port):
        try:
            self.conn = pymysql.connect(host=host, user=username, passwd=passwd, db=db_name, port=port, charset='utf8mb4')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("Cannot Connect To Mysql!/n", e)
            sys.exit()

    def insert(self, table, my_dict):
        try:
            self.cursor.execute("SET NAMES utf8mb4")
            cols = ', '.join(my_dict.keys())
            values = '"," '.join(my_dict.values())
            sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, cols, '"' + values + '"')
            try:
                result =
