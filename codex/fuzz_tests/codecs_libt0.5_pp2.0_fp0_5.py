import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='12341234',
                       db='testdb', charset='utf8mb4')

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

sql = """insert into customers(name, address)
         values (%s, %s)"""
# 매개변수로 값 넘기기
curs.execute(sql, ('둘리', '마이웨이로'))

# 매개변수 여러개 전달
curs.execute(sql, ('또치', '고양시'))


