import ctypes
import ctypes.util
import threading
import sqlite3
from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template
from flask import request
from flask import url_for
app = Flask(__name__)

from pprint import pprint

class PyLink:
    """
    This class is the main interface for PyLink.
    """

    def __init__(self, config=None):
        self.config = config or {}
        self.config['prefix'] = self.config.get('prefix', '')
        self.plugins = {}
        self.world = {}
        self.hooks = defaultdict(list)
        self.timers = []

        self.load_plugins()

        for plugin in self.plugins.keys():
            self.call_hooks('load', plugin=plugin)

    def load_plugins(self):
        """
        Loads plugins from the plugins.d/ subdirectory.
        """

        plugins_dir = os.path.join(os.getcwd(), 'plugins.d')
        if not os.path.exists(plugins_dir):
            os.mk
