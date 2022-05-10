import sys, threading

def run():
    sys.stdout.write(str(threading.current_thread().ident) + '\n')
    sys.stdout.write(str(threading.current_thread().name) + '\n')
    sys.stdout.write(str(threading.current_thread().daemon) + '\n')
    sys.stdout.write(str(threading.current_thread().is_alive()) + '\n')
    sys.stdout.write(str(threading.current_thread().ident) + '\n')
    sys.stdout.write(str(threading.current_thread().ident) + '\n')
    sys.stdout.write(str(threading.current_thread().ident) + '\n')
    sys.stdout.write(str(threading.current_thread().ident) + '\n')
    sys.stdout.write(str(threading.current_thread().ident) + '\n')
    sys.stdout.write(str(threading.current_thread().ident) + '\n')
   
