import socket

import click
import requests

from . import __version__
from .constant import DEFAULT_PATH


def get_host_ip():
    """
    get local ip address
    :return:
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def get_server_address(address):
    """
    get the server address
    :param address: the address of server
    :return:
    """
    if address is None:
        address = "http://{}:5000".format(get_host_ip())
    return address


@click.group()
@click.option('--address', '-a', help='The address of server', default=None)
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx, address):
    """
