import types
types.FileType
types.NoneType


sqlalchemy.orm.configure_mappers()

# Creates SQLAlchemy engine object

# SQLITE

# Local Sqlite 
# engine = sqlalchemy.create_engine("sqlite:///data/ims.db")


# MySql
engine = sqlalchemy.create_engine("mysql://root:!1010601@localhost/ims?charset=utf8")

# MSSQL
# engine = sa.create_engine('mssql+pyodbc://user:password@dsnname')

engine.echo = True

inspector= sqlalchemy.inspect(engine)


class Meta(object):

    def __init__(self, engine):
        self.metadata = sqlalchemy.MetaData(bind=engine)


class Base(object):

    def __init__(self, engine, tablename):
        
        self.metadata = Meta(engine).metadata
        self.Base = sqlalchemy.ext.declarative.declarative_base(
            metadata=self
