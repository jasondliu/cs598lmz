import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor

import requests

class UrlInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self, parent = None):
        super(UrlInterceptor, self).__init__(parent)

    def interceptRequest(self, info):
        url = info.requestUrl()
        url_str = url.toString()
        if url_str.startswith("https://api.laifudao.com/open/xiaohua.json"):
            info.block(True)
            print(f"block url: {url_str}")
        else:
            print(f"not block url: {url_str}")


class Page(
