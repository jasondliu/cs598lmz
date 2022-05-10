import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 存取密碼
with open('passwd.txt', 'r') as f:
    passwd = f.read().splitlines()[0]

# 連線資料庫
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd=passwd, db='mydb', charset='utf8mb4')

# 讀取資料庫內容
cur = conn.cursor()
sql = "SELECT * FROM `mytable`"
cur.execute(sql)

# 輸出資料庫內容
for r in cur:
    print(r)

# 關閉資料庫連線
cur.close()
conn.close()
 

# In[ ]:
