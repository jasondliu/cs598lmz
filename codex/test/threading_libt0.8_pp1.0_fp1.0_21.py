import threading
threading.Thread(target=cluster_app.app.run,args=('0.0.0.0',8000)).start()
threading.Thread(target=cluster_app.app.run,args=('0.0.0.0',8001)).start()
threading.Thread(target=cluster_app.app.run,args=('0.0.0.0',8002)).start()
threading.Thread(target=cluster_app.app.run,args=('0.0.0.0',8003)).start()
threading.Thread(target=cluster_app.app.run,args=('0.0.0.0',8004)).start()
threading.Thread(target=cluster_app.app.run,args=('0.0.0.0',8005)).start()
threading.Thread(target=cluster_app.app.run,args=('0.0.0.0',8006)).start()
