import socket
socket.if_indextoname(3)

#%%
import subprocess
device = subprocess.check_output("route | grep 0.0.0.0 | awk '{print $8}'", shell=True).strip()
device

#%%
import subprocess
output = subprocess.check_output("route | grep 0.0.0.0 | awk '{print $8}'", shell=True).strip()
output.decode("utf-8")

#%% [markdown]
# * **Cisco**
# * **Juniper**
# * **HP**
# * **Aruba**
# * **Fortinet**
# * **Arista**

#%%
from nornir import InitNornir

from nornir_scrapli.tasks import send_command
from nornir_scrapli.tasks import send_configs

from nornir.plugins.functions.text import print_title, print_result

from pprint import pprint
from datetime import datetime

from nornir.core.filter import F
from n
