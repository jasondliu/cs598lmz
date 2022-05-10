import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
device.installPackage('/home/liujiyu/Downloads/app-debug.apk')
# sets a variable with the package's internal name
package = 'com.example.xiaomage.xingvoices'
# sets a variable with the name of an Activity in the package
activity = 'com.example.xiaomage.xingvoices.feature.main.main.MainActivity'
# sets the name of the component to start
runComponent = package + '/' + activity
# Run the component
device.start
