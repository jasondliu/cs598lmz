import socket
# Test socket.if_indextoname('2')

import subprocess

import sys
# from .pypypy.interp_codewriter import read_target_trace
# from .pypypy.interp_codewriter import transform_target_ir
import time

from lxml import etree

import zipfile

# import pdb
# rpython -Ojit logtrans.py
def target(driver, args):
    # pdb.set_trace()
    # driver.exe_name = '%(platform)s/snl-rpython --stackless ' % driver.config.__dict__
    driver.exe_name = '%(platform)s/snl-rpython' % driver.config.__dict__
    driver.c_entryp_dict = {}
    # driver.c_entryp_dict['tp_apprun'] = '_pypy_app_tp_apprun'
    # driver.c_entryp_dict['tp_apprun_func'] = '_pypy_app_tp_apprun_func'
    driver.c_entryp_dict
