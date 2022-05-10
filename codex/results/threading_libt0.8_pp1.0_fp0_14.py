import threading
threading._DummyThread._Thread__stop = lambda x: 42

# this is a change

import webbrowser
import time

new=2
url="http://stackoverflow.com/questions/18561249/webbrowser-open-python-executable"
webbrowser.open(url,new=new)

time.sleep(5)

url="http://stackoverflow.com/questions/18561249/webbrowser-open-python-executable"
webbrowser.open(url,new=new)

webbrowser.open_new_tab(url)
</code>

