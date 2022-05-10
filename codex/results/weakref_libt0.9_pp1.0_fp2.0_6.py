import weakref
from sys import getsizeof
import gc
gc.set_debug(gc.DEBUG_LEAK)

def tracks_alive_weakrefs(seen_tracks, files):
    dead = set()
    for track_ref in seen_tracks:
        if track_ref() is None:
            dead.add(track_ref)
            continue
        track = track_ref()
        assert track.album is None
        assert track.genre is None

    seen_tracks -= dead

    # import sys
    # print("\n".join(list(map(str, [sys.getrefcount(x()) for x in list(seen_tracks)]))))
    # print("\n".join(list(map(str, [x() for x in list(seen_tracks)]))))


def tracks_alive_dict(seen_tracks, files):
    seen_tracks = [x for x in seen_tracks.values() if x.album]
    # print(seen_tracks)
    # import sys
    # print([sys.getrefcount(x) for x in seen_tracks])
