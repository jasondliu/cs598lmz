import socket
# Test socket.if_indextoname
# socket.if_indextoname(3)

###############################################################################
#
# Configuration for FTP tests

HOST = socket.gethostname()
if HOST == 'bsd5.test.python.org':
    FTP_HOST = 'ftp.freebsd.org'
    FTP_USER = 'anonymous'
    FTP_PASSWORD = 'test@test.test'
    FTP_HOME = '/pub/FreeBSD/'
    FTP_TEST_DIR = '/pub/FreeBSD/'
    FTP_TEST_FILE = '/pub/FreeBSD/README'
elif HOST == 'netbsd5.test.python.org':
    FTP_HOST = 'ftp.netbsd.org'
    FTP_USER = 'anonymous'
    FTP_PASSWORD = 'test@test.test'
    FTP_HOME = '/pub/NetBSD/'
    FTP_TEST_DIR = '/pub/NetBSD/'
    FTP_TEST_FILE = '/pub/NetBSD/README'
else:

