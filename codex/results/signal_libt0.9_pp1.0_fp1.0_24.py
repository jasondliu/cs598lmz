import signal
signal.signal(signal.SIGINT, signal_handler)
signal.alarm(30)
sys.path.append((os.getcwd()[:-7]))

from base.client import Client
from base.token import Token
from base.filter import Filter
from base.logging import Logging
from base.validation import Validation

from datetime import datetime
import pymysql
import sys

class Enrollment:
  def __init__(self):
    self.client = Client()
    self.logging = Logging()
    self.validation = Validation()
    self.filter = Filter()

  # GET Enrollment(s)
  def getEnrollment(self, token, enrollment_id):
    try:
      # Try to get the enrollment data
      query = "SELECT * FROM enrollment WHERE enrollment_id='%s'" % (enrollment_id)
      print(query)
      conn = self.client.getConn()
      with conn.cursor() as cursor:
        # execute the query
        cursor.execute(query)
       
