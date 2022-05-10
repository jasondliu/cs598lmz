import mmap

# The following constants are defined in the mod_wsgi spec.
# The first two are for request headers and the third for
# response headers.
#
AP_WAIT_TIMEOUT = 0
AP_READ_TIMEOUT = 0
AP_BUCKET_BUFFER = 0

# A list of headers which should not be transferred, but
# are used internally and should not be returned to client.
#
_bad_headers = [
        'Content-Length', 'Content-Type',
        'Transfer-Encoding', 'Upgrade',
        'Sec-WebSocket-Accept', 'Sec-WebSocket-Extensions',
        'Sec-WebSocket-Key', 'Sec-WebSocket-Version',
        'WebSocket-Extensions', 'WebSocket-Origin',
        'WebSocket-Protocol', 'WebSocket-Version',
    ]


