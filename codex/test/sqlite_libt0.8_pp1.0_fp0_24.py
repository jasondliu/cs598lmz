import ctypes
import ctypes.util
import threading
import sqlite3
import re
import traceback
import time

query_insert_device_event = "INSERT INTO device_event(name,value,flag) VALUES(?,?,?)"
query_delete_device_event = "DELETE FROM device_event WHERE "
query_delete_device_event_name = "name=? "
def add_query_delete_device_event_value(query,value):
    return query + " OR value=?"
def add_query_delete_device_event_flag(query,flag):
    return query + " OR flag=?"
def add_query_delete_device_event_name_value(query,name,value):
    if query == "":
        return "name=? AND value=?"
    else:
        return query + " OR (name=? AND value=?)"
def add_query_delete_device_event_name_flag(query,name,flag):
    if query == "":
        return "name=? AND flag=?"
    else:
        return query + " OR (name=? AND flag=?)"
