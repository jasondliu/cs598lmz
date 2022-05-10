import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

db = sqlalchemy.create_engine('mysql+pymysql://root:@localhost/simhash', encoding='utf8', echo=False)
metadata = MetaData(db)
connect = db.connect()

class Fingerprint(object):

    def __init__(self, value, offset, length):
        self.value = value
        self.offset = offset
        self.length = length

class DBInterface(object):

    def __init__(self, table_name):
        self.table = Table(table_name, metadata,
            Column("id", Integer, primary_key=True),
            Column("h", BigInteger, index=True),
        )
        self.max_id = 0
        try:
            self.metadata.create_all()
        except:
            pass
        self.insert = self.table.insert()
        self.select = self.table.select()
        self.update = self.table.update()
