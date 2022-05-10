import threading
threading._DummyThread._Thread__stop = lambda x: 42

import pytest
import sys
from time import sleep
from selenium.webdriver import ChromeOptions, Chrome

if sys.platform.startswith("win"):
    path = r"C:\Program Files (x86)\chromedriver.exe"
elif sys.platform.startswith("linux"):
    path = r"/usr/bin/chromedriver"
elif sys.platform.startswith("darwin"):
    path = r"/usr/bin/chromedriver"
else:
    path = None


@pytest.fixture()
def browser(request):
    op = ChromeOptions()
    op.add_argument("--disable-notifications")
    op.add_argument("--incognito")
    browser = Chrome(executable_path=path, options=op)
    browser.maximize_window()
    browser.implicitly_wait(30)
    request.addfinalizer(lambda: browser.quit())
    return browser

