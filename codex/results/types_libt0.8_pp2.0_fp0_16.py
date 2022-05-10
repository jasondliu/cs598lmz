import types
types.ModuleType.__init__.__defaults__ = (None,)
RC_HOST="http://rc.eosqa.com"
RC_PORT="80"
RC_VERSION="v1"
SKEY_FILE = "skey.txt"
TOKEN_FILE = "token.txt"

def get_rc_url():
    return RC_HOST+":"+RC_PORT+"/"+RC_VERSION

def load_skey():
    if os.path.exists(SKEY_FILE):
        with open(SKEY_FILE, "r") as skey_f:
            return skey_f.read()
    else:
        return None

def save_token(token):
    with open(TOKEN_FILE, "w") as token_f:
        token_f.write(token)

def load_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as token_f:
            return token_f.read()
    else:
        return None

def
