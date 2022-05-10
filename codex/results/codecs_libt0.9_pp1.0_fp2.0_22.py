import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import datetime
import subprocess


#DATE = datetime.datetime.now()
DATE = datetime.datetime(2015, 6, 1)

TODAY = datetime.date.today()
TODAY = datetime.date(TODAY.year, TODAY.month, TODAY.day)

MONTH = DATE.month
DAY = DATE.day
YEAR = DATE.year



#
# Initialize the Logging
#
initLogging(r"%s\%s.log" % (LOG_FOLDER, TODAY))

#
# Initialize the SFTP Server 
#
SFTPServer = Pysftp(host=SFTP_HOST, username=SFTP_USER, password=SFTP_PASSWORD)
SFTPServer.cwd(SFTP_REMOTE_FOLDER)
#print SFTPServer.pwd

#
# Read the configuration file
#

