import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

# 导入数据库配置
from config.conf import *

# 连接数据库
conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB, charset=CHARSET)

# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
# effect_row = cursor.execute("select * from tb7")

# 执行SQL，并返回受影响行数
# 注意：查询时，execute()返回结果集的行数，执行
