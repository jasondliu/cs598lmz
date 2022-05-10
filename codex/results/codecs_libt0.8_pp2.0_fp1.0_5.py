import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)



class newsDao:
    def __init__(self, config):
        self.config = config
        self.conn = conn = MySQLdb.Connect(
            host=config.get('database', 'db_host'),
            port=config.getint('database', 'db_port'),
            user=config.get('database', 'db_user'),
            passwd=config.get('database', 'db_pass'),
            db=config.get('database', 'db_name'),
            charset='utf8mb4'
        )
        self.cur = conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def insertNews(self, news):
        sql = "insert into scrapy_news(link, title, content, tag, category, publish_time, publish_source, author) values(%s, %s, %s, %s, %s, %s, %
