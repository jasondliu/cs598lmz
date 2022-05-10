import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='test', charset='utf8mb4')
cur = conn.cursor()

# 创建数据库
def create_database():
    cur.execute('DROP TABLE IF EXISTS `user`')
    sql = '''CREATE TABLE `user` (
              `id` int(11) NOT NULL AUTO_INCREMENT,
              `name` varchar(255) DEFAULT NULL,
              `password` varchar(255) DEFAULT NULL,
              PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1 ;
    '''
    cur.execute(sql)

