import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


class MySQLPipeline(object):
    """
    将数据存入MySQL
    """
    def __init__(self, db_name, db_user, db_pass, db_host, db_port, db_charset):
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_host = db_host
        self.db_port = db_port
        self.db_charset = db_charset

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            db_name=crawler.settings.get('MYSQL_DB_NAME', 'scrapy_db'),
            db_user=crawler.settings.get('MYSQL_DB_USER', 'root'),
            db_pass=crawler.settings.get('M
