import weakref


def clamp(val, min_val, max_val):
    return max(min(val, max_val), min_val)


def make_message(signature, *args):
    """Returns a DBus message with the given signature and arguments.

    :param signature: The signature of the message.
    :param args: Arguments to put in the message.
    :returns: A :class:`dbus.lowlevel.Message` object.
    """
    if isinstance(signature, str):
        signature = Signature(signature)
    msg = Message.new_method_call(DBUS_INTERFACE, DBUS_PATH, DBUS_INTERFACE,
                                  "GetAll")
    msg.append(DBUS_INTERFACE)
    msg.set_reply_handler(lambda *args: None)
    msg.set_auto_start(False)
    return msg


def _make_method(signature, method):
    # This is the actual method that's returned by the decorator
    def call_method(self, *args):
        reply_func
