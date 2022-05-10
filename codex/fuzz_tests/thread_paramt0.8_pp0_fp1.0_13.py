import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;31m')).start()
sys.dont_write_bytecode = True

import data, message, users

connection = data.database.connect('database.db')
database = connection.cursor()

message.load_modules()

users.init()

try:
    while True:
        raw_message_text = input('> ')
        message.parse(raw_message_text)
        connection.commit()
except KeyboardInterrupt:
    users.close()
