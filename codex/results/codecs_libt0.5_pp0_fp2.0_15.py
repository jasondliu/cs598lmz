import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# db = pymysql.connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     password='123456',
#     database='test',
#     charset='utf8mb4'
# )

db = pymysql.connect(
    host='192.168.10.65',
    port=3306,
    user='root',
    password='123456',
    database='test',
    charset='utf8mb4'
)

cursor = db.cursor()

sql = 'select * from user'

cursor.execute(sql)

# print(cursor.fetchone())
# print(cursor.fetchmany(2))
# print(cursor.fetchall())

# data = cursor.fetchall()
# print(data)
# for item in data:
#     print(item)

# for item in cursor.
