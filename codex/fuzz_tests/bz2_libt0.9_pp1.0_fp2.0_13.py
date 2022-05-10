import bz2
bz2.BZ2File.__init__
import dbm
dbm.gnu.open
open
eval('__builtins__')
eval('__builtins__').open
eval('__builtins__').open(filename)
thefile = eval('__builtins__').open(filename)
thefile
import marshal
import marshal
marshal.loads(thefile.read())
marshal.loads(thefile.read())['posts']
marshal.loads(thefile.read())['posts'][0]
marshal.loads(thefile.read())['posts'][0]['title']
for post in marshal.loads(thefile.read())['posts']:
print(post['title'])
for post in marshal.loads(thefile.read())['posts']:
print(post['title'])
for post in marshal.loads(thefile.read())['posts']:
print(post['title'])
for post in marshal.loads(thefile.read())['posts']:
print(post['title'])
import random
random.choice(
