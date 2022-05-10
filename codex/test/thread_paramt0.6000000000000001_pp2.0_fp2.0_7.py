import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
os.system('clear')

print("""
\033[1;32m 
  ____  _       _            
 |  _ \(_) __ _| | _____ _ __
 | |_) | |/ _` | |/ / _ \ '__|
 |  __/| | (_| |   <  __/ |   
 |_|   |_|\__, |_|\_\___|_|   
          |___/               
\033[1;32m 

Coded by: @Jayser_

""")

try:
    import requests
except ImportError:
    os.system('pip install requests')
    os.system('clear')
    os.system('python3 jayser_ddos_tool.py')

try:
    import random
except ImportError:
    os.system('pip install random')
    os.system('clear')
    os.system('python3 jayser_ddos_tool.py')

