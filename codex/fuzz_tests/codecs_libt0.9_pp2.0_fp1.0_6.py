import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
def sql2sql(config, sql, factor):
    print("正在判断数据集大小")
    cursor.execute("select count(*) from {}.{}".format(config['database'], config['table']))
    res = cursor.fetchall()[0][0]
    if res != 0:
        if factor == 'low':
            if res > 50000:
                print("数据集大小为{}条".format(res))
                print("正在修改数据集大小")
                sqls = "select * from {}.{} limit 50000".format(config['database'], config['table'])
                sql = re.sub(r'from ({0}.{1}).*'.format(config['database'], config['table']), r'from \1', sql)
            else:
                print("
