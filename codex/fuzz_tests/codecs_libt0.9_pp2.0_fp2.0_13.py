import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import not_


q = Queue()

id  = []

show_id  = []
show_name = []
show_sub = []
show_year = []
show_lang = []
show_season = []
show_seed = []
show_seedleech = []
show_magnet = []
show_thumb = []
show_desc = []
show_banner = []
show_fanart = []
episodes_id =[]
episodes_show_id = []
episodes_title = []
episodes_sub = []
episodes_date = []
episodes_magnet = []
episodes_thumb = []

def start_engine():
    global engine
    try:
        engine = create_engine('sqlite:///database.db')
        print 'Connected to Database'
        return True
    except:

