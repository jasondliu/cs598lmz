import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='test', charset='utf8mb4')
cursor = conn.cursor()

# 创建表
sql = """CREATE TABLE IF NOT EXISTS `test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1 ;"""
cursor.execute(sql)

# 插入数据
sql = "INSERT INTO test(name) VALUES(%s)"
cursor.execute(sql, ('测试'))
cursor.execute(sql, ('测
