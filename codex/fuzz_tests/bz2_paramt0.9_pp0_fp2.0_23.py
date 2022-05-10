from bz2 import BZ2Decompressor
BZ2Decompressor_methods = [
        '__init__',
        'decompress',
        ]

if sys.version_info[0] < 3:
    from Queue import Queue
    Queue_methods = [
        '__init__',
        'empty',
        'get',
        'put',
        'qsize',
    ]

    # Add the Queue iterator. Used in fileinput.
    import Queue
    Queue.Queue.__iter__ = Queue.Queue.__next__


else:
    from _queue import Queue
    Queue_methods = [
        '__init__',
        'empty',
        'get',
        'qsize',
        'task_done',
    ]
    Queue_attributes = [
        'queue',
    ]

if sys.version_info[0] < 3:
    from Cookie import CookieError
else:
    from http.cookies import CookieError
CookieError_methods = [
       '__init__',
       '__str__',
       ]

if
