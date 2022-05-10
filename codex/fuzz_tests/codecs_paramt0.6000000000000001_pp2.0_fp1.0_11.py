import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import time

from pygame import mixer

from . import util
from . import gmail


def make_display_string(email):
    """Create a display string from an email object."""
    if hasattr(email, 'subject'):
        subject = email.subject
    else:
        subject = 'No Subject'

    if hasattr(email, 'from_addr'):
        from_addr = email.from_addr
    else:
        from_addr = 'Unknown'

    return '{} from {}'.format(subject, from_addr)


def notify(email):
    """Display a notification for the given email."""
    notif = pynotify.Notification(make_display_string(email),
                                  email.body,
                                  'mail-message-new')
    notif.show()


def play_sound():
    """Play the sound for a new email."""
    mixer.init()
    mixer.music.load('/usr/share/sounds/freed
