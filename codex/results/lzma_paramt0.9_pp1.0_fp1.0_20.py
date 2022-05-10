from lzma import LZMADecompressor
LZMADecompressor() # bug in hexchat-python 2.9.9

# TODO: consider making this a user option
SILENT = True

PLUGIN_NAME = 'cbzoom'


class ChannelHandler(object):
    def __init__(self, context):
        self.context = context

    def connect(self, ip, port):
        self.sender = CloudbotSocket(ip, port)

        # Send join command
        self.sender.send(b'\x01')
        self.sender.receive()

    def join(self, channel):
        """Joins a channel, creating the channel object and printing connect message on channel"""
        print(f'Joining channel {channel}')
        channel_name = self.context['channels'][0].get_name()
        self.sender.send(f'\x04-#{channel_name}'.encode('utf-8'))
        data = self.sender.receive()

        # Extract channel number
        channel_number = data[1]

        # Extract joined=False/True from
