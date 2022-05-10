import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 关于时间的操作
import datetime
# 计算两个日期的天数差
def get_date_diff(start, end):
    s = datetime.datetime.strptime(start, "%Y-%m-%d")
    e = datetime.datetime.strptime(end, "%Y-%m-%d")
    diff = e - s
    return diff.days

# 计算两个日期的月数差
def get_month_diff(start, end):
    s = datetime.datetime.strptime(start, "%Y-%m")
    e = datetime.datetime.strptime(end, "%Y-%m")
    diff = (e.year - s.year)*12 + e.month - s.month
    return diff

#
