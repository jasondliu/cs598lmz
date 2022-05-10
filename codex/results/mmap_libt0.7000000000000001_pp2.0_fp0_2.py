import mmapi;
import sys;
import os;
import os.path;
import re;
import traceback;
import jsmin;
import json;
import time;
import threading;
import zipfile;

class JsFile:
    def __init__(self, file_path, file_name):
        self.file_path = file_path;
        self.file_name = file_name;
        self.is_min = file_name.endswith('.min.js');
        self.min_file_name = file_name[:-3] + '.min.js';
    def get_file_name(self):
        return self.file_name;
    def get_file_path(self):
        return self.file_path;
    def get_min_file_name(self):
        return self.min_file_name;
    def get_is_min(self):
        return self.is_min;
    def set_is_min(self, is_min):
        self.is_min = is_min;
    def update(
