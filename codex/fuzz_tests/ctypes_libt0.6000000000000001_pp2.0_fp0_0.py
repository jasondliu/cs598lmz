import ctypes
ctypes.windll.user32.LockWorkStation()

## Restart
import os
os.system('shutdown /r /t 1')

## Shutdown
import os
os.system('shutdown /s /t 1')

## Logout
import os
os.system('shutdown /l')

## Hibernate
import win32com.client
win32com.client.Dispatch('WScript.Shell').SendKeys('%{F4}')

## Sleep
import win32com.client
win32com.client.Dispatch('WScript.Shell').SendKeys('%{F1}')

## Taskmanager
import os
os.system('taskmgr')

## Run
import os
os.system('run')

## CMD
import os
os.system('cmd')

## CMD
import os
os.system('cmd')

## Notepad
import os
os.system('notepad')

## Calculator
import os
os.system('calc')

## Paint
import os
os.system('mspaint')

## Command Prompt
import
