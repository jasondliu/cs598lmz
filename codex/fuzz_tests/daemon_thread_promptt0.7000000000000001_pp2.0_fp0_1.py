import threading
# Test threading daemon:
import time

def daemon():
    print "Starting daemon..."
    while True:
        time.sleep(2)
        print "Daemon running..."

t = threading.Thread(target=daemon)
t.setDaemon(True)
t.start()

# [END] Test threading daemon

# Set up a dictionary to hold information about the
# application we are building (name, version, platform, etc).
g_app_info = {
    'name': 'Buddy',
    'version': '1.0.0',
    'platform': 'None',
    }

# Declare the supported options.
parser = OptionParser()
parser.add_option("-p", "--platform", dest="platform", help="set the platform type", metavar="PLATFORM")
(options, args) = parser.parse_args()

# Set the platform type.
if options.platform:
    g_app_info['platform'] = options.platform

# Initialize the app.
app = wx.App(0)

# Make a new frame
