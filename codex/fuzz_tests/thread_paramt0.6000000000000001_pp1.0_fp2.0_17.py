import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a')).start()

import webbrowser
webbrowser.open("http://www.python.org")

import webbrowser
webbrowser.open("http://www.python.org", new=2)

import webbrowser
webbrowser.open("http://www.python.org", new=0)

import webbrowser
c = webbrowser.get("firefox")
c.open("http://www.python.org")


import webbrowser
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("/usr/bin/firefox"))
webbrowser.get('firefox').open_new_tab("http://www.python.org")

import webbrowser
webbrowser.open_new("http://www.python.org")

import webbrowser
webbrowser.open_new_tab("http://www.python.org")

import webbrowser
webbrowser.open_new("http://www.python.org")

import webbrowser
webbrowser.open_new
