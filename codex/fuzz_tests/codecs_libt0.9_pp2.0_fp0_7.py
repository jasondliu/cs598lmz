import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

db = MySQLdb.connect(
    host='52.193.146.188',
    port=3306,
    user='root',
    passwd='root',
    db='test',
    charset='uft8mb4'
)

cursor = db.cursor();
sql = "select * from employees;"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()
db.close()
