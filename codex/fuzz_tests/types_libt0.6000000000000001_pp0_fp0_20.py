import types
types.ClassType = type
from com.ziclix.python.sql import zxJDBC
from java.lang import Class
from java.sql import DriverManager, SQLException
from java.util import Hashtable
import sys
import string


url = 'jdbc:oracle:thin:@localhost:1521:orcl'
driver = 'oracle.jdbc.driver.OracleDriver'
username = 'system'
password = 'oracle'

try:
    jdbc_args = [url, username, password]
    jdbc_class = Class.forName(driver)
    jdbc_conn = DriverManager.getConnection(*jdbc_args)
    connection = zxJDBC.connect(jdbc_conn, None, None)
    cursor = connection.cursor()

    print "Connected to Database"
except SQLException, e:
    print "Error: %s" % e
    sys.exit(1)


def get_query(table_name):
    """
    Returns query to get the table data
    """

