import mmap
import logging
import csv
import re
import os
import sys

from . import command

class Ghidra(command.Command):

    def __init__(self):
        self.export_path = os.path.join(os.getcwd(), "database/ghidra")
        self.db_path = os.path.join(self.export_path, "database")
        self.db_diff_path = os.path.join(self.export_path, "database_diff")
        self.db_old_path = os.path.join(self.export_path, "database_old")
        self.db_new_path = os.path.join(self.export_path, "database_new")

        self.filtered_name = []
        self.filtered_hash = []

        if not os.path.isdir(self.export_path):
            os.makedirs(self.export_path)

    def help(self):
        print("Usage: ghidra")

    def auth(self, database):
        database = database
