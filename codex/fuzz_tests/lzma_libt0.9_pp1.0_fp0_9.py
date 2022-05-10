import lzma
lzma.open
import gzip

# need to check if program is run as root
if os.geteuid() != 0:
    exit('You need to have root privileges')

# get server information
url = ""
username = ""
password = ""

# get url
url = raw_input('web url: ')

# get user info
f = open('user.txt')
for line in f:
    username,password = line.split(':')

# create the password manager
# TODO: add the certificate manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
top_level_url = url
password_mgr.add_password(None, top_level_url, username, password)

handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib2.build_opener(handler)

# use opener to download a resource
opener.open(url)

# Install the opener.
# Now all calls to ur
