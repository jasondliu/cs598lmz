import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import sys


class DB:

    def __init__(self, host, name, user, password, port=None):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.port = port
        self.connection = self.connect()

    def connect(self):
        if self.port:
            return pymysql.connect(host=self.host,
                                   user=self.user,
                                   password=self.password,
                                   db=self.name,
                                   charset='utf8',
                                   cursorclass=pymysql.cursors.DictCursor,
                                   port=self.port)
        else:
            return pymysql.connect(host=self.host,
                                   user=self.user,
                                   password=self.password,
                                   db=self.name,
                                   charset='utf8',
                                  
