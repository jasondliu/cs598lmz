import types
types.ModuleType.__str__ = lambda self: ""
import yaml

os.path.sep = '/'

error = {}

now = datetime.datetime.now()

def formate_date(timestamp):
    now = datetime.datetime.now()
    if  now.year - timestamp.year > 0:
        return timestamp.strftime('%Y-%m-%d %H:%M:%S')
    if  now.month - timestamp.month > 0:
        return timestamp.strftime('%m-%d %H:%M:%S')
    if  now.day - timestamp.day > 0:
        return timestamp.strftime('%m-%d %H:%M:%S')
    if  now.hour - timestamp.hour > 0:
        return '%d小时前' %(now.hour - timestamp.hour)
    if  now.minute - timestamp.minute > 0:
        return '%d分钟前' %(now.minute - timestamp.minute)
