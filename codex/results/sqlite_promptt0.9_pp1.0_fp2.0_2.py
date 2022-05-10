import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:') for in-memory mode
import os

# Now = "2019-06-27"
# print(Now.split('-'))
# out = Now.split('-')
# for _ in range(4-len(out)):
#     out.append('')
# month = out[1]
# print(out)
# print(len(out))

# # print([str(int(month)).rjust(2, '0')][0])
#
# months = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля',
#           '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа',
#           '09': 'сентября', '10': 'октября', '11': 'ноября', '12':
