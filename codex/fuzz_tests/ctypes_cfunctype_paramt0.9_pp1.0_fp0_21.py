import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def run_callback_async(callback, *args, **kwargs):
    """
    Run a callback in a subthread with a timeout of 25 seconds.

    Note that the callback function should always returns in less than 25
    seconds or else the thread will be terminated and an error will be logged.

    This is to prevent an invalid callback that may hang, e.g., when a file is
    not found.
    """

    if callback:
        subthread = threading.Thread( target=lambda callback=callback: \
                                        callback(*args, **kwargs) )
        subthread.daemon = True
        subthread.start()

def parse_json(json_file_content):
    """
    Parse JSON file.

    Return the parsed JSON file on success, otherwise, return None.
    """
    content = None
    try:
        content = json.loads(json_file_content)
    except:
        pass
    finally:
        return content

def formatDateTime(dateTime):
    return dateTime.strftime("%Y-%m-
