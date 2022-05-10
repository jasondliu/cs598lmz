from bz2 import BZ2Decompressor
BZ2Decompressor()
from zlib import decompress
from io import BytesIO

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

from models import Base, Article, Body, Publication, Category, User
from data_cleanup import regex_cleaner, remove_entry, remove_entries, regex_cleaner_num, create_category_map

from sqlalchemy.exc import IntegrityError
%load_ext sql
%config SqlMagic.autocommit=False

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from model import Base, Article, Body, Publication, Category, User
from data_cleanup import regex_cleaner, remove_entry, remove_entries, regex_cleaner_num, create_category_map
    
engine = create_engine('mysql+pymysql://root:boogie123@
