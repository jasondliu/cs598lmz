import sys, threading

def run():
    global mtr
    mtr = __import__("mtr", fromlist=["app"])
    mtr.app.main()

t = threading.Thread(target=run)
t.start()

import gtk
import appindicator

def menu_response(w, buf):
    mtr.app.terminate(None, None)
    gtk.main_quit()

def menu_about(w, buf):
    mtr.app.showAbout(None, None)

if __name__ == "__main__":
    indicator = appindicator.Indicator("example-simple-client",
                                       "indicator-messages",
                                       appindicator.CATEGORY_APPLICATION_STATUS)
    indicator.set_status(appindicator.STATUS_ACTIVE)
    indicator.set_attention_icon("indicator-messages-new")
    indicator.set_icon("indicator-messages")
    indicator.set_label("MTR")

    menu = gtk.Menu()

    item_quit = g
