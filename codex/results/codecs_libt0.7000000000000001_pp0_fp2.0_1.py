import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def main():
    # mysql_master = Mysql(host, username, password, database, port)

    mysql_slave = Mysql(host, username, password, database, port)
    # sql = "select * from user"
    # result = mysql_slave.getAll(sql)
    # print result

    # sql = "select * from user limit 3"
    # result = mysql_slave.getOne(sql)
    # print result

    # sql = "select * 
