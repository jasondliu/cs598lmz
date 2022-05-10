import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import sublime
import sublime_plugin
import os.path

_async_lock = threading.Lock()

_config = {}

_db = None
_db_lock = threading.Lock()

_nontranslating_fields = ['project']

def plugin_loaded():
    load_config()
    open_db()

def load_config():
    global _config

    try:
        _config = sublime.load_settings('awesome-pl.sublime-settings')
    except IOError:
        # so far everything is optional, so let's carry on
        pass

def plugin_unloaded():
    global _config, _db

    try:
        _db.close()
    except:
        pass

TIP_SHOWN = 'show_sentence_translate_tip_shown'
TIPS = {
    'en': 'Highlight a sentence and press <kbd>%s</kbd> to translate it.',
    'pl': 'Zaznacz zdanie i wciśnij <
