import weakref

from . import _util
from ._util import (
    _get_default_session,
    _make_method_return_future,
    _method_docs,
)
from .aiohttp_transport import AIOHTTPTransport
from .exceptions import (
    ClientError,
    Forbidden,
    HTTPException,
    NotFound,
    ServerError,
    Unauthorized,
)
from .models import (
    AuditLog,
    AuditLogDiff,
    AuditLogEntry,
    AuditLogEntryType,
    AuditLogs,
    Avatar,
    Bans,
    BaseModel,
    Channel,
    ChannelInvite,
    ChannelType,
    Colour,
    Connection,
    ContentFilter,
    Emoji,
    Game,
    Guild,
    GuildBan,
    GuildEmoji,
    GuildEmojiUpdate,
    GuildIntegration,
    GuildMember,
    GuildPreview,
    GuildRole,
    Invite,
    InviteMetadata,
    InviteTargetUserType,
    InviteWithMetadata,

