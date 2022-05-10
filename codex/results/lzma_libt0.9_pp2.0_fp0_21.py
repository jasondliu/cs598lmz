import lzma
lzma.open = lzma.LZMAFile

from gi.repository import PackageKitGlib as pk
def query_pkgs(filters, pk_callback, pk_data=None):
    try:
        filters = pk.Filter(filters)
        client = pk.Client()
        client.connect_sync(None)
        client.resolve_async(filters, None, pk_callback, pk_data)
    finally:
        client.disconnect()

def install_update_pkgs(filters):
    filters = pk.Filter(filters)
    client = pk.Client()
    client.connect_sync(None)
    try:
        pk.install_packages(client, True, filters, None)
    finally:
        client.disconnect()

def get_uninstalled_pkgs(filters):
    try:
        packages = []
        install_filters = []
        state = {
            'filter_installed': False
        }

        def pk_callback(client,
