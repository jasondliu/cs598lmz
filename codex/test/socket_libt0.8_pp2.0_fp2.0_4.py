import socket


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

WEB_IP = '192.168.8.125'
#WEB_IP = 'localhost'
WEB_PORT = 4666

DEBUG = True

#
# sqllite
#
DB_NAME = 'database.db'

#
# web
#
TEMPLATES_AUTO_RELOAD = True
SECRET_KEY = 'ai18'
