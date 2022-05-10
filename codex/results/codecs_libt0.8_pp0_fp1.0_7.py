import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

catalog = "./catalog.db"

db = sqlite3.connect(catalog)

cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL)''')
db.commit()

def insert_user(email, name, password):
    try:
        cursor.execute('''INSERT INTO users(email, name, password)
                        VALUES(?,?,?)''', (email, name, password))
        db.commit()
        return "User inserted"
    except:
        return None

def get_user(email):
    cursor.execute('''SELECT name, email, password FROM users WHERE email = ?''', (email,))
    return cursor.fetchone()

def update_user(email, name
