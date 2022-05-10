import mmap
import re
import os

#清理缓存
def clean_cache():
    if os.path.exists('./cache.txt'):
        os.remove('./cache.txt')

#获取缓存
def get_cache():
    return open('cache.txt', 'r')

#写入缓存
def write_cache(text):
    with open('cache.txt', 'a') as f:
        f.write(text)

#查找pattern在filename中出现的页码
def find_page_no(filename, pattern):
    #查找出第一个匹配的字符串
    first_match = next(re.finditer(pattern, filename)).start()
    page_begin = filename.rfind('<pagenum>', 0, first_match)
    page_end = filename.find('</pagenum>', page_begin)
