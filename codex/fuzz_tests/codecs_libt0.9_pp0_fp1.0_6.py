import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# This file allows to setup the database in case you haven't already done it.

# You must have created the file "secrets.sh". This file contains all the secret 
# information like the username of you database and its password. It allows us to 
# make those public.

# Import the secrets.sh file ...
from secrets import *

# ... which contains all the secret information
# It is an array of 3 elements
# - USERNAME: your database username
# - PASSWORD: your database password
# - KEY_FILE: the authentication file that python has to use in order to connect to the database
#             this is to facilitate the connection, so you don't have to type your username and password at each reboot
# - HOST_NAME: the name or the ip addr of the machine hosting the database

# The following lines import the needed modules to establish a connection to the database
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql
