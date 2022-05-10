import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class MySqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', 'root', 'scrapy_db', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""INSERT INTO scrapy_db.scrapy_data (title, link, date, content) VALUES (%s, %s, %s, %s)""",
                            (item['title'].encode('utf-8'),
                             item['link'].encode('utf-8'),
                             item['date'].encode('utf-8'),
                             item['content'].encode('utf-8')))

            self.conn.commit()

        except MySQLdb.Error, e:
            print "Error %d: %
