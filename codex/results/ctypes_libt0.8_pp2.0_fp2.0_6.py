import ctypes
ctypes.windll.kernel32.SetConsoleTitleA("WARNING")
import os
os.system("cls")

file = "ccv.db"
def create_table():			#Arxikopoihsh tou arxeiou, dhmiourgia pinakwn
    cursor.execute('CREATE TABLE IF NOT EXISTS accounts(acct VARCHAR(255) NOT NULL UNIQUE, pin INTEGER NOT NULL, balance REAL DEFAULT 0)')
    cursor.execute('CREATE TABLE IF NOT EXISTS transactions(trans_id INTEGER PRIMARY KEY AUTOINCREMENT, acct VARCHAR(255) NOT NULL, ')
    cursor.execute('timestamp VARCHAR(255) NOT NULL, amount REAL NOT NULL, balance_after REAL NOT NULL, trans_type VARCHAR(255) NOT NULL)')
create_table()

def deposit(acct, am, pin):
    cursor.execute('SELECT balance FROM accounts WHERE acct=? AND pin=?', (acct, pin))
    try:
        balance = cursor.fetchone()[0
