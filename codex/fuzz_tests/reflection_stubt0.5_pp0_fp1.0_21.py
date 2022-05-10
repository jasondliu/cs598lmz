fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

# Create a frame
frame = fn.__code__.co_filename, fn.__code__.co_firstlineno, fn.__code__.co_name, '', None
frame = frame[0], frame[1], frame[2], frame[3], frame[4]

# Create a traceback
traceback = (frame, None, None)

# Create an exception
exception = ZeroDivisionError()

# Create a context
context = exception, traceback, None, None

# Create a log record
record = LogRecord('name', Logger.INFO, 'pathname', 1, 'msg', (), None, None, context)

# Create a logger
logger = Logger('name')
logger.addHandler(StreamHandler())

# Log
logger.handle(record)

# Check that the traceback is printed
print('ok')
