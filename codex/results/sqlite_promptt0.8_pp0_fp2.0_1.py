import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
print "sqlite3 version: " + sqlite3.version
print "sqlite3 shell version: " + sqlite3.sqlite_version

# Test ldap.initialize
ldap.initialize('ldap://localhost:389')
# Test ldap.set_option
ldap.set_option(ldap.OPT_X_TLS_NEWCTX, 0)

# Test ldap.get_option
ldap.set_option(ldap.OPT_X_TLS_NEWCTX, 1)
ldap.get_option(ldap.OPT_X_TLS_NEWCTX)

try:
	# Test python-ldap v3.0+ features
	ldap.get_option(ldap.OPT_PROTOCOL_VERSION)
except ldap.LDAPError, e:
	if e.message[0]['desc'] == 'Undefined option or bad option':
		# No support for getting protocol version
		pass
	else:
		raise e

try:
	#
