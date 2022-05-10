import gc, weakref
from json import JSONDecodeError

from flask import g
from flask_restful import Resource, reqparse
from googletrans import Translator
from pywikibot import Page

from config import bot_config, pywiki_config, flask_config, DATA_DIR
from config.texts import DEFAULT_LANGUAGE, LANGUAGES
from utils import make_logger
from utils.request_watcher import RequestWatcher
from utils.wiki_bot import WikiBot
from utils.flask_utils import make_request_watcher
from utils.google_utils import get_google_translator

LOG = make_logger("translate")


# Helper functions
def get_default_translator():
    return Translator(service_urls=['translate.google.com', 'translate.google.co.kr'])


def is_supported(language):
    return language in bot_config.get('supported_languages', [])


def main_languages():
    language_data = pywiki_config.get_data("languages
