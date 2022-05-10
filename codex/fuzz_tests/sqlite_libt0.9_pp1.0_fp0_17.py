import ctypes
import ctypes.util
import threading
import sqlite3

URL=lambda name: "http://acm.hdu.edu.cn/contests/"+name+"/problem/"+name[:-1]+"-"
login_url=lambda username,password,name: '''http://acm.hdu.edu.cn/userloginex.php?action=login&username={username}&userpass={password}&login=Sign+In'''.replace('{username}',username).replace('{password}',password).format(cid=name)
problem_url=lambda username,password,problem_id,name: '''http://acm.hdu.edu.cn/contests/{name}/status.php?first=&pid={problem_id}&user={username}&lang=0&status=0'''.format(username=username,password=password,problem_id=problem_id,name=name)

class Status:
    def __init__(self,username,password,name,maxnum):
        self.username=username
        self.password=password
        self.name=name
        self.maxnum=max
