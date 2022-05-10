import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
run_dir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(run_dir, '..')))

from config import get_config
from db import get_db_session
from model import Base, User, Post, Tag, Post_tag, Comment
from utils import get_logger

logger = get_logger(__name__)

def init_db():
    """
    Initialize the database
    """
    logger.info("Initializing the database...")
    config = get_config()
    engine = create_engine(config.get("db", "db_url"), echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)


def drop_db():
    """
    Drop the database
    """
    logger.info("Dropping the database
