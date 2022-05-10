import weakref

from gui import gui_constants


def memoize(f):
    """Memoization decorator for a function taking a single argument"""
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__


class Sound:
    def __init__(self, sound_path):
        self.sound_path = sound_path
        self.buffers = {}
        self.player = None
        self.loop = False
        self.gain = 1.0

    def play(self, loop=False):
        self.stop()
        self.loop = loop
        self.player = pyglet.media.Player()
        self.player.eos_action = pyglet.media.Player.EOS_LOOP if loop else pyglet.media.Player.EOS_STOP
        self.player.queue(self.get_source())
        self.player.play()

    def stop(self):
        if self.player is
