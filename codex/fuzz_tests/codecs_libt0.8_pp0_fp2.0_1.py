import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import os
import re

def get_abspath(mypath):
    '''获取脚本的绝对路径'''
    return os.path.join(os.path.dirname(__file__), mypath)


def get_abspath_curfile():
    '''获取脚本文件的绝对路径'''
    return os.path.abspath(__file__)

#获取当前目录
def get_current_dir():
    return os.path.dirname(__file__)


def get_current_dir_file(filename):
    '''返回当前目录下文件的绝对路径'''
    return os.path.join(os.path.dirname(
