import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 为了显示中文，需要以下代码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# 创建数据库连接
conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='test', charset='utf8mb4')
cur = conn.cursor()

# 创建查询语句
sql = '''
select
    `order`.order_id as orderId,
    `order`.create_time as orderCreateTime,
    `order`.order_status as orderStatus,
    `order`.pay
