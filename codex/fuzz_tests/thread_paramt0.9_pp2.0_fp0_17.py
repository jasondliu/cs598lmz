import sys, threading
threading.Thread(target=lambda:sys.stdout.write('')).start()
from collections import Counter
import pandas as pd, matplotlib.pyplot as plt, os, pyodbc, datetime, json, operator
from datetime import datetime as dt


class Data():
    def __init__(self, directories, db='K&J COVID-19', server='DESKTOP-0N49N31\SQLEXPRESS'):
        self.dir = directories
        self.db = db
        self.server = server
        self.conn = pyodbc.connect(Driver='{SQL Server}',server=self.server,Trusted_Connection='Yes',database=self.db)
        self.curs = self.conn.cursor()
        self.q = {}
        self.q['Confirmed-Cases-per-100,000-people'] = "SELECT date FROM countries WHERE country = '"+self.country+"'"
        self.q['Deaths-per-100,000-people'] = "SELECT date FROM countries WHERE country = '"+self.country+"'"

