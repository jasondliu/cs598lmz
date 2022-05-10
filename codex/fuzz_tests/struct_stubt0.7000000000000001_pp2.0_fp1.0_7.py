from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i4sh')
s.pack(1, 2, 3)

# 复合结构：元组
# 数据库：sqlite3，充当持久存储的内存数据库，不存储在磁盘上
import sqlite3

# 复合结构：数据库连接
conn = sqlite3.connect('test.db')

# 创建游标
c = conn.cursor()

# 插入数据
c.execute("insert into test values (1, 'test')")

# 查询数据
for row in c.execute('select * from test'):
    print(row)

# 提交事务
conn.commit()

#
