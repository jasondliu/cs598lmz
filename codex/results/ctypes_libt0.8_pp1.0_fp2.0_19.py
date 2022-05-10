import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("iMazing main backup")
import shutil, os
from sys import argv
import argparse
import datetime
import subprocess

# Setup
parser = argparse.ArgumentParser()
parser.add_argument("--backupDir",help="The device backup dir",default=r"C:\ProgramData\Apple\MobileSync\Backup")

args = parser.parse_args()

backupdir = args.backupDir

if not os.path.isdir(backupdir):
    print('Couldnt find backupdir, please ensure its correct')

#####
print('Looking for latest backup...')

maxdate = 0
latestbackup = ''
for di in os.listdir(backupdir):
    if os.path.isdir(backupdir+'\\'+di):
        val = datetime.datetime.strptime(di, '%Y-%m-%d-%H%M%S').timestamp()
        
        if val > maxdate:
            maxdate = val
            latest
