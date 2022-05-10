import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# MySQL Connection
host = "localhost"
user = "root"
password = "root"
db = "test"
port = 3306

conn = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8mb4', port=port)

# SQL 문장
sql = "select * from test"

# 커서 생성
curs = conn.cursor()

# SQL 실행
curs.execute(sql)

# 데이터 Fetch
rows = curs.fetchall()
print(rows)

# Connection 닫기
conn.close()
