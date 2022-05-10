import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# conn = sqlite3.connect('fetchmail.sqlite3')
# conn.execute('CREATE TABLE IF NOT EXISTS fetchmail(id INTEGER PRIMARY KEY, user TEXT, mail TEXT, subject TEXT, fromd TEXT)')
# conn.commit()
# conn.close()

# Test poplib
# from poplib import POP3
# from email.mime.text import MIMEText
# from email.header import decode_header
# mailserver = POP3('mail.sina.com')
# mailserver.user('user')
# mailserver.pass_('pass')
# print('Messages: %s. Size: %s' % mailserver.stat())
# resp, mails, octets = mailserver.list()
#
# print(mails)
#
# index = len(mails)
# resp, lines, octets = mailserver.retr(index)
#
# msg_content = b'\r\n'.join(lines).decode('utf-8')
# msg = Parser().parsest
