import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import pymysql

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'test',
    charset = 'utf8mb4'
)

cur = conn.cursor()

cur.execute("SELECT * FROM `test`")

for row in cur:
    print(row)

cur.close()
conn.close()
</code>

