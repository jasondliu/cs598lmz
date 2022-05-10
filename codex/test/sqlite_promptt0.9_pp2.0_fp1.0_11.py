import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# deprecated
# class DDRParser(HTMLParser.HTMLParser):
#     def __init__(self):
#         HTMLParser.HTMLParser.__init__(self)
#         self.data = ""
#         self.urls = []
# 
#     # only links from same hostname allowed
#     def handle_starttag(self, tag, attrs):
#         if tag == "a":
#             for attr in attrs:
#                 if attr[0] == "href":
#                     if attr[1] != "javascript:void(0);" and attr[1] != "#":
#                         self.urls.append(attr[1])
# 
#     def handle_data(self, data):
#         self.data += data
# 
#     def get_data(self):
#         return self.data.encode("utf-8")
# 
#     def get_urls(self):
#         return self.urls

