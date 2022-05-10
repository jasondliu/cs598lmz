import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db")

# Modules
import config
import ciphers
import users
import hmac_sha1

# Global variables

# Functions
def init():
	config.load("server.conf")
	ciphers.init()
	users.init()
	hmac_sha1.init()

def shutdown():
	config.save("server.conf")
	ciphers.shutdown()
	users.shutdown()
	hmac_sha1.shutdown()

def main():
	init()
	
	shutdown()

if __name__ == "__main__":
	main()
