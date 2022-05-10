import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# import os
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# import cx_Oracle
# db = cx_Oracle.connect('username/password@host:port/sid')
# cursor = db.cursor()
# cursor.execute('select * from table')
# for row in cursor:
#     print(row)
# cursor.close()
# db.close()

# import cx_Oracle
# db = cx_Oracle.connect('username/password@host:port/sid')
# cursor = db.cursor()
# cursor.execute('select * from table')
# for row in cursor:
#     print(row)
# cursor.close()
# db.close()

# import cx_Oracle
# db = cx_Oracle.connect('username/password@host:port/sid')
# cursor = db.cursor()
# cursor.execute('select * from table')
#
