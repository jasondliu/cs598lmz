import weakref

from olm import Account, InboundGroupSession

from .events import NEW_GROUP_SESSION


class GroupSessionStore:
    """Custom stores to use for group sessions.

    Group session decryption requires key material to be stored in a InboundGroupSession
    object. If the object goes out of scope in the process of handling an event,
    the HS will crash.

    To work around this, we store the inbound group sessions in a weakly-referenced dict,
    keyed by the session ID.
    
    Inspired by `@sorunome's work <https://github.com/matrix-org/olm/commit/bafe718b64947fa4212459adb7ca43b8fd8fd18b>`_
    """
    def __init__(self, sync_handler, log):
        self.sync_handler = sync_handler
        self.log = log
        self.store = {}
        for event in sync_handler.sync_forward_extremities:
            session = InboundGroupSession()
            session.unpickle(event["content
