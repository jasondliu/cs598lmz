import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import pymysql
pymysql.install_as_MySQLdb()

# import MySQLdb
# MySQLdb.install_as_MySQLdb()

# import pymysql
# pymysql.install_as_MySQLdb()

# import MySQLdb
# MySQLdb.install_as_MySQLdb()

# import pymysql
# pymysql.install_as_MySQLdb()

# import MySQLdb
# MySQLdb.install_as_MySQLdb()

# import pymysql
# pymysql.install_as_MySQLdb()

# import MySQLdb
# MySQLdb.install_as_MySQLdb()

# import pymysql
# pymysql.install_as_MySQLdb()

# import MySQLdb
# MySQLdb.install_as_MySQLdb()

# import pymysql
# pymysql.install_as_My
