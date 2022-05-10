import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# create database connection
db = create_engine('mysql+pymysql://root:root@localhost:3306/mysql')

# create metadata object
metadata = MetaData(db)

# create table object
users = Table('user', metadata, autoload=True)

# create query
query = select([users.c.User, users.c.Host, users.c.Password]).where(users.c.User == 'root')

# execute query
result = db.execute(query)

# print result
for row in result:
    print('User:', row[0])
    print('Host:', row[1])
    print('Password:', row[2])
    print('-' * 80)
