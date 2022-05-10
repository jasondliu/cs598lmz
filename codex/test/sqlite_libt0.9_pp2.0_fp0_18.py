import ctypes
import ctypes.util
import threading
import sqlite3


class TCPDream(threading.Thread):
    def __init__(self,local=True):
        super(TCPDream, self).__init__()
        self.local = local
        self.con = sqlite3.connect('config.db')
        self.cur = self.con.cursor()
        self.cur.execute("select * from config where 1")
        configs = self.cur.fetchall()
        self.sport = int(configs[0][1])
        self.saddr = str(configs[0][2])
        self.dport = int(configs[0][3])
        self.daddr = str(configs[0][4])
        self.target = (self.daddr,self.dport)

    def run(self):
        if self.local:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.saddr, self.sport))
            s.listen(0)
            s,addr=s.accept
