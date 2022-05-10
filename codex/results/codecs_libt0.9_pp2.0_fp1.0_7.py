import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

class Download:
    def __init__(self, config):
        self.host = config['host']
        self.db = config['db']
        self.user = config['user']
        self.password = config['password']
        self.table = config['table']

        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def run(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * from {}'.format(self.table))
            result = cursor.fetchall()
        self.connection.close()

        for date_index, date in enumerate(self.get_date_range()):
            self.remove_file_if_ex
