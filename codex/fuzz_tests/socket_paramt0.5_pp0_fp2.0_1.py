import socket
socket.if_indextoname(3)

#read config file
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

#get ip address
import netifaces as ni
ni.ifaddresses('en0')
ip = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']

#get mac address
import uuid
mac = uuid.getnode()

#get hostname
import socket
hostname = socket.gethostname()

#get port number
port = config['DEFAULT']['port']

#get username
username = config['DEFAULT']['username']

#get password
password = config['DEFAULT']['password']

#get interface
interface = config['DEFAULT']['interface']

#get logfile
logfile = config['DEFAULT']['logfile']

#get logfile
logfile = config['DEFAULT']['logfile']

#get logfile
logfile = config['DEFAULT']['logfile']

#get logfile
logfile =
