import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

HOST = 'localhost'
USER = 'root'
PASSWORD = 'root'
DATABASE = 'zhihu'

QUESTION_TABLE = 'question'
ANSWER_TABLE = 'answer'
COMMENT_TABLE = 'comment'

class DBHelper(object):

    def __init__(self, host=HOST, user=USER, password=PASSWORD, database=DATABASE):
        try:
            self.conn = MySQLdb.connect(host=host, user=user, passwd=password, db=database, charset='utf8mb4')
            self.cursor = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

        except MySQLdb.Error as e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def insert_question(self, question_id, title, detail, created_time
