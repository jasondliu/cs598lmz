import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# import MySQLdb
# conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='test', charset='utf8mb4', use_unicode=True)
# cur = conn.cursor()
# cur.execute("SELECT * FROM test_table")
# cur.close()
# conn.close()

import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', passwd='', db='test', charset='utf8mb4', use_unicode=True)
cur = conn.cursor()
cur.execute("SELECT * FROM test_table")
cur.close()
conn.close()
</code>

