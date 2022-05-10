import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/Users/micha.suda/Library/ShareExtension/ShareExtension.storedata/ShareExtension.storedata')
import datetime

app_group_id = 'group.com.zauberstuhl.ShareExtension'

def get_identifier():
    if AppKit.NSUserDefaults.alloc().initWithSuiteName_(
            app_group_id).objectForKey_('identifier'):
        return AppKit.NSUserDefaults.alloc().initWithSuiteName_(
            app_group_id).objectForKey_('identifier')
    else:
        return '0'
    
def set_identifier(identifier):
    AppKit.NSUserDefaults.alloc().initWithSuiteName_(
        app_group_id).setObject_forKey_(identifier, 'identifier')
    
    
def sql_save(data):
    if data['type'] == 'url':
        sql = 'INSERT INTO items (type, timestamp, text, URL) VALUES (?,?,?,?)'
