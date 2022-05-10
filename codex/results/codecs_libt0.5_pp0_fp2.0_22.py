import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up database
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/weibo?charset=utf8mb4')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Weibo(Base):
    __tablename__ = 'weibo'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(20))
    weibo_url = Column(String(255))
    created_at = Column(DateTime)
    like_num = Column(Integer)
    repost_num = Column(Integer)
    comment_num = Column(Integer)
    content = Column(String(255))
    user_description = Column(String(255))
    user_
