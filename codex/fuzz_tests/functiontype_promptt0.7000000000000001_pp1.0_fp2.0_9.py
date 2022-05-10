import types
# Test types.FunctionType for the record
# TODO: change to a method decorator
def record(name=None):
    """
    Decorator that records the function call and return value.
    """
    def _record(func):
        if name is None:
            name = func.__name__
        def wrapper(*args, **kwargs):
            started = time.time()
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                status = 'FAILED'
                exception = e
            else:
                status = 'SUCCESS'
                exception = None
            finally:
                ended = time.time()
                duration = ended - started
                record = Record(name, status, args, kwargs, result, exception, duration)
                log.info(record.to_json())
            if status == 'FAILED':
                raise exception
            return result
        return wrapper
    return _record
