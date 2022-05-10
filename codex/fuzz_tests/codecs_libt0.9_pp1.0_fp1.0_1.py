import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from django.core.management import execute_from_command_line#导入所有的模块和函数

import os
import sys


file_path = os.path.normpath(os.path.dirname(__file__))
os.chdir(file_path)
sys.path.insert(0,'..')#把个人项目路径加入环境变量，以便能够被django读取到


if __name__ == '__main__':
    #os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guest.settings')#让os获取环
