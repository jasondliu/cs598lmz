import _struct, string
from time import time

from m2pressed import common
from m2pressed import players


def m2p():
    return M2P()


def find_player(players, search):
    """
    Search a list of players for one with the specified properties. Useful
    for retrieving the ID of a player when creating a new playlist.
    """
    for p in players:
        if not set(search.items()).difference(p.items()):
            return p
    return None


def is_compat(version):
    """Checks if the given compatibility version is compatible with the
    installed version of m2pressed. Raises an IndexError exception if the
    version is incompatible.
    """
    try:
        compat_version = common.get_compatibility()
    except Exception:
        # Shouldn't happen. In the future, we may be able to use the
        # application version as a backup.
        pass
