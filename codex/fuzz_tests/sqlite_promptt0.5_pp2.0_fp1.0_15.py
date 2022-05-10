import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db")

import unittest

from . import common

class ThreadTests(common.TestCase):

    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        self.cur = self.con.cursor()
        self.cur.execute("create table test(i)")
        self.con.commit()

    def tearDown(self):
        self.cur.close()
        self.con.close()

    def CheckPragma(self, cur):
        cur.execute("pragma synchronous=off")
        cur.execute("pragma journal_mode=off")
        cur.execute("pragma locking_mode=exclusive")

    def CheckCommit(self, con):
        con.commit()

    def CheckRollback(self, con):
        con.rollback()

    def CheckSelect(self, cur):
        cur.execute("select * from test")
        cur.fetchone()

    def CheckInsert(self, cur):
        cur.execute("insert into test(i)
