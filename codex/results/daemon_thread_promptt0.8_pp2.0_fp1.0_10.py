import threading
# Test threading daemon 
#import httplib
#import urllib2
import webbrowser

# set up the database
db = sqlite3.connect('wappDB') # note there is no file extension 
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS wapp_log
             (id integer primary key autoincrement, date text, name text, url text, path text, size integer, type text)''')
db.commit()

# globals
db_lock = threading.RLock()


# send a push notification
def send_push(name, text):
	if WEB_PUSH_KEY != '':
		os.system('curl -d \'{"text":"'+name+': '+text+'"}\' https://api.pushbullet.com/v2/pushes -u '+WEB_PUSH_KEY+': >/dev/null 2>&1 &')
	else:
		print('No Web Push Key set, please set the WEB_PUSH_KEY in the config.py file')


