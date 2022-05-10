import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


class Database:
    def __init__(self):
        try:
            # Connect to DB
            self.connection = pymysql.connect(host='localhost',
                                              user='root',
                                              password='1234',
                                              db='project',
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            print(e)

    def execute(self, query, args={}):
        try:
            # execute query
            with self.connection.cursor() as cursor:
                query = cursor.mogrify(query, args)
                cursor.execute(query)
                self.connection.commit()
        except Exception as e:
            # print(e)
            pass

    def executeOne(self, query, args={}):
        try:
            # execute query
            with self.connection.cursor()
