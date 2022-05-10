import threading
threading.stack_size(2**27)

def run_in_background(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread
    return wrapper

def run_in_foreground(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.daemon = False
        thread.start()
        return thread
    return wrapper

def run_in_background_with_timeout(timeout):
    def decorator(func):
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=func, args=args, kwargs=kwargs)
            thread.daemon = True
            thread.start()
            thread.join(timeout)
            return thread
        return wrapper
    return decorator

