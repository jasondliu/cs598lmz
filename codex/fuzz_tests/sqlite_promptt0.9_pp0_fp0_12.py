import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db") 생
# UpdateDB.write(helpList) 생 
# UpdateDB.get_help_list() 반환형 : [[idx, name, teacher, contact, place, startDate, endDate, place, category, car, meal]]
# UpdateDB.get_help_list(idx=) 반환형 : [[idx, name, teacher, contact, startDate, endDate, place, category, car, meal]]
# UpdateDB.now_help(idx)
# UpdateDB.now_not_help(idx)
# UpdateDB.add_category('무엇')
# UpdateDB.add_category(['무엇', '다음'])
# UpdateDB.remove_category('무엇')
# UpdateDB.remove_category(['무엇', '다음'])
# UpdateDB.add_member(chat_id, first_name, last_name='', username='', email='', gender='',
