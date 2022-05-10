import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 生产环境
# pool = redis.ConnectionPool(host='10.10.69.170', port=6379, db=0)
# r = Redis(connection_pool=pool)

# 开发环境
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
r = Redis(connection_pool=pool)


# 添加到list
def add_data(table, data):
    r.lpush(name=table, *data)


# get list datas
def get_all_data(table):
    return r.lrange(table, 0, -1)


# clear list data
def clear_data(table):
    r.delete(table)


# 添加到sets
def add_data_set(table, data):
    r.sadd(
