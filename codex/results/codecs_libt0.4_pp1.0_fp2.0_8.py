import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='1234',
                       db='python_app1', charset='utf8mb4')

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# SQL문 실행
sql = "select * from users"
curs.execute(sql)

# 데이타 Fetch
rows = curs.fetchall()
print(rows)     # 전체 rows
# print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
# print(rows[1])  # 두번째 row: (2, '강수
