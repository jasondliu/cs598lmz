import lzma
lzma.MAX_LENGTH = 2**42
import requests
import os
import shutil

__author__ = 'Aska'


class MainSys(object):
    def __init__(self, sysname, mainsys):
        self.sysname = sysname
        self.mainsys = mainsys
        self.sysinfofile = mainsys.sysinfofile
        self.sysinfos = mainsys.sysinfos
        self.path_initsize = self.path_init()

    def path_init(self):
        temppath = os.getcwd()
        try:
            os.chdir(self.sysname)
        except FileNotFoundError:
            os.mkdir(self.sysname)
            os.chdir(self.sysname)
        path = os.getcwd()
        os.chdir(temppath)
        return path

    def system(self):
        temppath = os.getcwd()
        os.chdir(self.path_initsize)
        while True:
