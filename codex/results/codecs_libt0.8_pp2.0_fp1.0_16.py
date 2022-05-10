import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

conn = MySQLdb.Connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = 'root',
        db = 'douban',
        charset = 'utf8')

cursor = conn.cursor()

try:
    cursor.execute('select * from book')
    results = cursor.fetchall()
    for r in results:
        print r[0], r[1], r[2]
except:
    print "Error"
