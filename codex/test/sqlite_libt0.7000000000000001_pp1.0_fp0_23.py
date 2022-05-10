import ctypes
import ctypes.util
import threading
import sqlite3

# Disable the default SSL certificate verification
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class AntiSpamPlugin(gajim.plugins.GajimPlugin):
    def init(self):
        self.gui_extension_points = {'chat_control_base' : (self.connect_chat_control,
            self.disconnect_chat_control)}

        self.config_dialog = None

        # Default settings
        self.config = {
            'check_urls': False,
            'check_fake_urls': False,
            'check_urls_in_message': False,
            'check_urls_in_nick': False,
            'check_urls_in_status': False,
            'check_keywords': False,
            'keywords': None
        }

        self.chat_controls = []
        self.instances = []

