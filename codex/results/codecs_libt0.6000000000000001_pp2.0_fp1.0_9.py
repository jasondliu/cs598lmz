import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'root',
    db = 'spider_python',
    charset = 'utf8'
)

# 创建游标
cursor = conn.cursor()

# 定义sql语句
sql = '''
    create table if not exists students(
        id int unsigned primary key auto_increment,
        name varchar(20) not null,
        gender enum('m','f') not null,
        age tinyint unsigned not null default 18,
        score int unsigned not null default 0,
        remark varchar(60)
    )engine=innodb default charset=utf8;
'''

# 执行sql语句
cursor.execute
