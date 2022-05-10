import weakref
import re

from aqt import mw

def load(browser):
    import my_browser_menu_items

    try:
        if browser.isCloze():
            menu = browser.form.menuEdit
        else:
            menu = browser.form.menuEdit
        a = QAction(mw)
        a.setText("Delete current card")
        a.triggered.connect(lambda : my_browser_menu_items.delete_card(browser, browser.selectedCards()))
        menu.addAction(a)

        a = QAction(mw)
        a.setText("Delete selected cards")
        a.triggered.connect(lambda : my_browser_menu_items.delete_card(browser, browser.selectedCards()))
        menu.addAction(a)

    except Exception as e:
        print('Error in BrowserMenuSetup (Browser.py):', e)

addHook("browser.setupMenus", load)

#from anki.hooks import addHook
#from aqt.qt import *
#from
