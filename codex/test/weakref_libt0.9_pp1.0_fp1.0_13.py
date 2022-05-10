import weakref

fname = 'private_chat_mod.py'

class PrivateChatMod(Module):
    """Allow commands in private message."""

    def init(self, *args):
        self.default_options.update({
            # If set to True, channel private is ignored, else only
            # private are accepted
            'ignore_channel_private': False,
        })

        # Init keystore
        self.keystore = Keystore(self.name)
