import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#to get the current directory
import os
os.getcwd()

#to get the current directory with the file name
import os
os.path.realpath(__file__)

#to get the current directory with the file name
import os
os.path.abspath(__file__)

#to get the current directory with the file name
import os
os.path.dirname(os.path.realpath(__file__))

#to get the current directory with the file name
import os
os.path.dirname(os.path.abspath(__file__))

#to get the current directory with the file name
import os
os.path.dirname(__file__)

#to get the current directory with the file name
import os
os.path.dirname(os.path.abspath(__file__))

#to get the current directory with the file name
import os
os.path.dirname(os.path.realpath
