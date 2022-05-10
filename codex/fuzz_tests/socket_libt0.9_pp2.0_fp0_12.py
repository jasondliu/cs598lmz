import socket
import time


def ping_client_async(channel_name, callback):
    """
    Publishes a ping message, then sets up its callback.

    :param channel_name: channel to ping
    :param callback: function to be called upon Message receive
    """
    pubnub.publish(channel=channel_name, message="hello!!", callback=callback, error=callback)


def time_loop():
    """
    Perfo
