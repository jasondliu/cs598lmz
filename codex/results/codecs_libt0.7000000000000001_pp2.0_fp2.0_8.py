import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import time
import datetime
import re
import sys
import math


# 根据输入的日期计算周几
def get_week_day(date):
    week_day_dict = {
        0: '周一',
        1: '周二',
        2: '周三',
        3: '周四',
        4: '周五',
        5: '周六',
        6: '周日',
    }
    day = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    return week_day_dict[day]


def get_courses_list(json):
    elements = json['elements']
    courses = []
    for element in elements:
        if element['elementType'] == 'course':
            courses.append
