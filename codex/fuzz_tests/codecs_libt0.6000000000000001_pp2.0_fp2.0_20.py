import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:root@localhost:3306/test', encoding='utf8mb4', echo=True)
conn = engine.connect()
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, String, Integer, DateTime
class Article(Base):
    __tablename__ = 'article'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    url = Column(String(255))
    pub_time = Column(DateTime)
    
    def __repr__(self):
        return 'id: %s, title: %s, url: %s, pub_time: %s' % (self.id
