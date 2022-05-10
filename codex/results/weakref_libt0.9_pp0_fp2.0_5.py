import weakref

import asyncio

from ..event import EventHandler
from ..event import ServerEvent
from ..event import ChannelEvent
from ..event import PresenceEvent
from ..event import StatusEvent
from ..permissions import Permissions


__all__ = ('TextChannel', 'VoiceChannel', 'Category')


class Channel(Base):
    """

    """
    __slots__ = ('id', 'name', 'mention', 'position', 'server', 'parent',
                'permissions_put', 'permissions_overwrite')

    def __init__(self, *, data, guild):
        self.id = int(data['id'])
        self.server = guild
        self.parent = None
        self.update_data(data)

    def permission_for(self, user):
        allow_bits = 0
        deny_bits = 0
        puts = self.permissions_put.get(user.id, None)
        overwrites = self.permissions_overwrite.get(user.id, None)
        if overwrites is not None:
            if overwrites.get('type
