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
        try:
            self.keystore.open()
        except Exception, e:
            self.log.warn('could not open keystore (%s), '
                          'private_msg will work only once')

        # Save the password
        self.keystore.set_get('password', '', 'a password to set to the bot')
        # Add the callback
        self.add_input_hook(self.handle_input, 99)

    def close(self, *args, **kwargs):
        self.keystore.set('password', self.bot.passwd)
        self.keystore.save()
        self
