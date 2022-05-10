import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# mysql
# engine = create_engine('mysql://root:root@localhost:3306/test', echo=True)
engine = create_engine('mysql://root:root@localhost:3306/test?charset=utf8mb4', echo=True)

# sqlite
# engine = create_engine('sqlite:///:memory:', echo=True)

# postgresql
# engine = create_engine("postgresql://scott:tiger@localhost/test", echo=True)

# mssql
# engine = create_engine("mssql+pymssql://scott:tiger@hostname:port/dbname", echo=True)

# oracle
# engine = create_engine("oracle://scott:tiger@127.0.0.1:1521/sidname", echo=True)

# firebird
# engine = create_engine("firebird://sysdba:masterkey@localhost/C
