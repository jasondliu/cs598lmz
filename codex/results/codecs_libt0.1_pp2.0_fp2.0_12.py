import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test', charset='utf8mb4')
cursor = conn.cursor()

# 创建表
sql = """
CREATE TABLE IF NOT EXISTS `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""
cursor.execute(sql)

# 插入数据
sql = "INSERT INTO user(username, password) VALUES (%s, %s)"
cursor.execute(sql,
