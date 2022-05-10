import mmap
import re
import time
import sys

# Tested on Windows 7
#
# Test this by running a command prompt as Administrator, then running:
#
#   netsh wlan start hostednetwork
#
# Then run this script.
#
# You'll need to install pcapy and impacket:
#
#   pip install pcapy
#   pip install impacket
#
# I had to copy
#
#   C:\Python27\Lib\site-packages\impacket\examples\secretsdump.py
#
# to
#
#   C:\Python27\Scripts\secretsdump.py
#
# This is because impacket is installed for Python 2.7, but this script
# uses Python 3.4.

def run(command):
    print('Running: {}'.format(command))
    return subprocess.check_output(command, shell=True)

def get_adapter_name():
    output = run('netsh wlan show hostednetwork')
    match = re.search(r'Hosted network settings\s+:\s+Name
