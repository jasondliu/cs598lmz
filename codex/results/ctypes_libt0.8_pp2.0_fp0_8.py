import ctypes
ctypes.windll.kernel32.SetConsoleTitleW('python')

class User:
    def __init__(self, uid, name, balance, score):
        self.uid = uid
        self.name = name
        self.balance = balance
        self.score = score
        self.used = 0

def get_user_info(uid):
    f = 'user/' + uid + '.txt'
    if os.path.exists(f):
        with open(f) as file:
            info = file.readlines()
            name = info[0].strip()
            balance = info[1].strip()
            score = info[2].strip()
            try:
                balance = int(balance)
                score = int(score)
            except:
                balance = 0
                score = 0
            return User(uid,name,balance,score)
    else:
        return None

def check_user(uid):
    f = 'user/' + uid + '.txt'
    if os.path.exists(f):
        return True

