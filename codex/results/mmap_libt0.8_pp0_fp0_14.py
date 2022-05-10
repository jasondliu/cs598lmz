import mmap
import sys

def get_offset(file_object):
    file_object.seek(0)
    return file_object.tell()

def set_offset(file_object, offset):
    file_object.seek(offset)

def fill_chunk(file_object, data):
    file_object.write(data)

def dump_mem(file_object, offset=0, size=0):
    file_object.seek(offset)
    return file_object.read(size)

def dump_mem_chunk(file_object, offset=0, size=0):
    file_object.seek(0)
    file_object.seek(offset)
    return file_object.read(size)

def dump_search_mem(file_object, search_string):
    file_object.seek(0)
    file_object.seek(file_object.read().find(search_string))
    return file_object.read(1)

def fill_search_mem(file_object, search_string, data):
    file_object
