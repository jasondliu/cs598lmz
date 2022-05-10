import threading
threading.Thread(target=keepRunning).start()

"""
    使用 XMLRPC 服务器时，我们只需要编写相应的类，并将类注册到这个服务器上，
    然后客户端就可以通过这个服务器访问这个类的相应方法了。
"""
