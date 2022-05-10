import socket
import time
import requests

global uid, token, devicename, deviceip, deviceport, devicepublicip

#N.B. You need to create a device on the IoT cloud platform, and insert the device name
# and device token here to run the program
#device name:
devicename = 'demo2'
#device token:
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NzgzOTUwNjUsImRhdGEiOnsidXNlcklkIjoiN2U0MGY1ZTAtMjI4OC00MDIwLThlYzEtYTY4NmI4NDIxYjZmIiwiZGV2aWNlSWQiOjIwMDY5fX0.HjhsxFDDgL2zeZ0nKjQ2Jl0nyyNsV7rwOJfmhOj7p_U"

#Get device information

