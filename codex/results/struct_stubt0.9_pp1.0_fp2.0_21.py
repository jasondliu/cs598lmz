from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', endian='<')
f='cccc'

from selenium import webdriver
options = webdriver.ChromeOptions()
# options.add_argument('load-extension=/path/to/extension/directory')
options.add_argument('--auth-server-whitelist="http://127.0.0.1:5000"')
options.add_argument('--auth-and-launch-app="http://127.0.0.1:5000"')
options.add_argument('--disable-web-security')
options.add_argument('--user-data-dir=/tmp/chrome_insecure')
chrome_prefs = {}
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
options.experimental_options["prefs"] = chrome_prefs
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537
