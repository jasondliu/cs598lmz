import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int32, ctypes.c_int32)
f = FUNTYPE(lambda x, y: print('x=%s, y=%s' % (x, y)))
f.argtypes = None
f(1, 2)
x = 1
x = 0
print(x)

from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, create_engine

metadata = MetaData()
user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String),
             Column('fullname', String),
             )
address = Table('address', metadata,
                Column('id', Integer, primary_key=True),
                Column('user_id', None, ForeignKey('user.id')),
                Column('email_address', String, nullable=False)
                )
engine = create_engine('mysql://root:root@localhost:3306/test')
mcb=sql.MetaBase(engine)
mcb.engine.connect()
metadata.create_all(engine
