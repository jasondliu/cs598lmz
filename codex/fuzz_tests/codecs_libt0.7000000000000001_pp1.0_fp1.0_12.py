import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import os
from config import config
from urllib.request import urlretrieve

from webapp import app
import webapp.views
from webapp.utils.get_tweets import get_tweets
from webapp.utils.get_likes import get_likes
from webapp.utils.get_follows import get_follows
from webapp.utils.get_followers import get_followers
from webapp.utils.get_destination import get_destination
from webapp.utils.recommend import recommend
from webapp.utils.tag_cloud import get_tag_cloud
from webapp.utils.get_news import get_news
from webapp.utils.get_blog_posts import get_blog_posts
from webapp.utils.get_weather import get_weather
from webapp.utils.get_events import get_events
from webapp.utils.get_facts import get_facts


app.jinja_env.globals.
