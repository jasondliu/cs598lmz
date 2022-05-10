import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='spider', charset='utf8mb4')
cursor = conn.cursor()

# 执行查询语句
sql = "select * from bilibili_video"
cursor.execute(sql)

# 提取数据
result = cursor.fetchall()

# 关闭连接
cursor.close()
conn.close()

# 打印结果
print(result)

# 将数据转换为DataFrame
df = pd.DataFrame(list(result))
df.columns = ['id', 'title', 'author', 'play_num', 'danmu_num
