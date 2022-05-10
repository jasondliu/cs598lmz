import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# c.execute('drop table if exists users')
# c.execute('create table users (name text, age int)')
# c.execute('insert into users (name, age) values (?, ?)', ('John', 30))
# c.execute('insert into users (name, age) values (:name, :age)', {'name': 'Jane', 'age': 35})
# c.execute('select * from users')
# for row in c.fetchall():
#     print row
# conn.commit()
# conn.close()
# Test opencv
# import cv2
# cap = cv2.VideoCapture(0)
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # Display the resulting frame
#     cv2.imshow('frame',frame)
#     print cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT), cap.get(cv2.
