import threading
threading.activeCount()

class Mysql_server:
    def __init__(self):
        self.db_name=input("请输入数据库名称:")
        try:
            self.conn = MySQLdb.Connect(host="localhost", user="root", passwd="123456", db=self.db_name, charset="utf8")
        except:
            print("数据库连接失败")
        self.cursor = self.conn.cursor()
        self.table_name=input("请输入表名:")
        # self.table_name="test"
        self.table_state=''
        self.label_state=''
        self.get_table_state()
        self.get_label_state()
        print(self.table_state)

    def get_label_state(self):
        sql = "select * from %s" % self.table_name
        self.cursor.execute(
