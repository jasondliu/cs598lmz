import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#
# Configuration
#

# db connection
db_config = {
    'user': 'root',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'test',
}

#
# Main
#

class Model:
    def __init__(self, db):
        self.db = db

    def get_name(self, name):
        query = "select * from names where name = %s"
        cursor = self.db.cursor()
        cursor.execute(query, (name,))
        return cursor.fetchone()

    def add_name(self, name):
        query = "insert into names (name) values (%s)"
        cursor = self.db.cursor()
        cursor.execute(query, (name,))
        self.db.commit()


if __name__ == '__main__':
    try:
        # connect to db

