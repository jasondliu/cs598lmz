import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8mb4')
# 创建游标
cursor = conn.cursor()

# 创建数据库
cursor.execute("DROP DATABASE IF EXISTS `%s`" % 'douban_movie')
cursor.execute("CREATE DATABASE `%s` DEFAULT CHARACTER SET utf8mb4" % 'douban_movie')
cursor.execute("USE `%s`" % 'douban_movie')

# 创建表
cursor.execute("""
    CREATE TABLE `%s` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `rank` INT NOT NULL,
       
