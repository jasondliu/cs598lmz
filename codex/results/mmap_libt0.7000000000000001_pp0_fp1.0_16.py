import mmap
import errno
import os
import sys
import pwd
import grp

def get_file_contents(filename):
    with open(filename, 'r') as f:
        return [line.rstrip() for line in f]

def get_current_user():
    return pwd.getpwuid(os.getuid())[0]

def get_current_group():
    return grp.getgrgid(os.getgid())[0]

def get_file_owner(filename):
    return pwd.getpwuid(os.stat(filename).st_uid).pw_name

def get_file_group(filename):
    return grp.getgrgid(os.stat(filename).st_gid).gr_name

def get_file_type(filename):
    return os.stat(filename).st_mode

def get_file_permissions(filename):
    return oct(os.stat(filename).st_mode)[-3:]

def get_file_size(filename):
    return os.
