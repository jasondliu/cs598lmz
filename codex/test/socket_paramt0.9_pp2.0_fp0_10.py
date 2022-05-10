import socket
socket.if_indextoname("3")

from dns import reversename
from dns import resolver

def getIP(s):
  rev = reversename.from_address(s)
  try:
    ip = str(resolver.query(rev,"PTR")[0])
    return ip[:-1]
  except:
    return False

from tkinter import *
root = Tk()
root.title("DNS")
root.geometry("1000x500")

from tkinter import filedialog

from tkinter import messagebox
def alert(title,message):
  messagebox.showinfo(title,message)

def getConfig():
  global int_mac_table, enable_password, line_password, login_password, config

  result = filedialog.askopenfilename()

  with open(result,'r') as f:
    lines = f.readlines()
  
