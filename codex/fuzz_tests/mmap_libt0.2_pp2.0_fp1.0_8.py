import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from bs4 import BeautifulSoup
import requests

from lib import util
from lib import config
from lib import database
from lib import log
from lib import web

class Manga(object):
    def __init__(self, manga_id, manga_name, manga_url, manga_cover, manga_status, manga_last_chapter, manga_last_chapter_url, manga_last_update, manga_last_check, manga_added_date, manga_tags, manga_rating, manga_description, manga_author, manga_artist, manga_genres):
        self.manga_id = manga_id
        self.manga_name = manga_name
        self.manga_url = manga_url
        self.manga_cover = manga_cover
        self.manga_status = manga_status
        self.manga_last_chapter = manga_last_chapter
        self.manga_last_chapter_url = manga_last
