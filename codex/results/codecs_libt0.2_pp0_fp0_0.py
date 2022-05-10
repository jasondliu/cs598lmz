import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='test', charset='utf8mb4')
cursor = conn.cursor()

# 创建表
sql = """CREATE TABLE IF NOT EXISTS `test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""
cursor.execute(sql)

# 插入数据
sql = "insert into test(name,age) values(%s,%s)"
cursor.execute(sql, ('test', 10))

#
