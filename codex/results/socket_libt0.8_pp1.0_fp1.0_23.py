import socket
import time
import os
import glob
import datetime
import threading

# create a folders to store the data
if not os.path.exists("Data"):
    os.makedirs("Data")

if not os.path.exists("Data/On_board"):
    os.makedirs("Data/On_board")

if not os.path.exists("Data/Off_board"):
    os.makedirs("Data/Off_board")

#list all files in the folder On_board
list_On_board = os.listdir("Data/On_board/")
number_of_On_board =len(list_On_board)
print(number_of_On_board)
#list all files in the folder Off_board
list_Off_board = os.listdir("Data/Off_board/")
number_of_Off_board =len(list_Off_board)
print(number_of_Off_board)
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket
