import socket
import re
import operator
import datetime
import csv

#Define the function to print the hostname and IP address
def get_host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ",host_name)
        print("IP : ",host_ip)
    except:
        print("Unable to get Hostname and IP")

#Define the function to extract the time and date from a string
def time_extract(string):
    #Define the regex to extract the time from a string
    time_regex = re.compile(r'\d{2}:\d{2}:\d{2}')
    #Define the regex to extract the date from a string
    date_regex = re.compile(r'\d{2}-\d{2}-\d{4}')
    #Define the regex to extract the date and time from a string
