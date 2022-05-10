import socket
import threading
from .app import app
from .db import db
from .handlers.api import api_handler


def create_app(config_object=None):
    app.config.from_object(config_object)
    db.init_app(app)
    api_handler.init_app(app)
    return app


def run_serve():
    # 创建socketserver服务
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer(('127.0.0.1', 5000), app)
    server.serve_forever()


def run_nginx():
    # 启动nginx
    nginx_path = os.path.join(app.config['NGINX_PATH'], 'nginx.exe')
