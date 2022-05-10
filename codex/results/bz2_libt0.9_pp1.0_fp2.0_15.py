import bz2
bz2.open(open('file.bz2')).read()

#cx_Oracle
from cx_Oracle import SessionPool
import cx_Oracle

class Oracle:
    def __init__(self):
        os.environ["NLS_LANG"] = ".UTF8" #设置环境变量，解决oracle 编码问题
    def connOracle(self):
        dsn=cx_Oracle.makedsn('10.18.0.130',1521,'orcl') #创建数据源名
        self.conn=cx_Oracle.connect('hztb2','hztb2', dsn) #链接数据库，用自己的用户名，密码，数据源名
        self.cursor=self.conn.cursor()
    def selectOracle(self
