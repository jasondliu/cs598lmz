import selectors
import sys
import types

'''
The Echo Server

The server has two responsibilities:

- Serve the file to the client.
- Receive responses from the client and write them to a log file.

The server will send the client the file one line at a time. When the entire
file has been sent, the client will begin sending responses to the server. The
client will send one response per line of the file. When the file has been
completed, the client will send a final message, which the server will use to
close the connection. The server will write client responses to a log file in
the same directory as the server. The client responses should be in the same
order as the file lines.
'''

fileName = sys.argv[1]

sel = selectors.DefaultSelector()
# messages_to_send = []

# Note: we're using our own custom 'ExampleProtocol' object, instead of one
# of the standard library protocols, to simplify the example and get rid of
# some boilerplate code.
class ExampleProtocol(asyncio.Protocol):
    def __
