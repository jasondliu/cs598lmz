import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='mysql', charset='utf8mb4')

# 创建游标
cur = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cur.execute("select * from user")

# 打印结果
print(effect_row)

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cur.close()

# 关闭连接
conn.
