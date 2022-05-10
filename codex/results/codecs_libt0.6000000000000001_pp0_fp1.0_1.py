import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

class MySQL(object):
    """
    This class is used for connecting to the MySQL database.
    """

    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        """
        Initializes the MySQL database connection.
        """
        try:
            self.connection = MySQLdb.connect(db=db_name, user=db_user, passwd=db_password, host=db_host, port=db_port, charset='utf8mb4')
            self.connection.autocommit(True)
            self.cursor = self.connection.cursor()
        except MySQLdb.OperationalError, message:
            print "Error %d:\n%s" % (message[0], message[1])
            exit()

    def query(self, query):
        """
        Queries the database.
        """
        cursor = self.connection.cursor(MySQLdb.c
