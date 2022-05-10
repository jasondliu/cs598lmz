import gc, weakref

# ===
# Forward references.
# ===

class Base:
    def __init__(self, on_ca_error, on_ca_connection_made, on_ca_connection_lost):
        self._on_ca_error = on_ca_error
        self._on_ca_connection_made = on_ca_connection_made
        self._on_ca_connection_lost = on_ca_connection_lost
        self._ch = None
        self._pvs = None
        self._pvs_by_name = None
        self._pvs_by_ch = None
        self._pvs_by_pv = None
        self._pvs_by_alias = None
        self._pvs_by_alias_value = None
        self._in_update_callback_processing = False
        self._is_connected = False
        self._pvs_need_updating = False
        self._pvs_update_requests = None # Dictionary of Channel-to-ChannelUpdateRequest
        self._pvs_update_tasks = None # Dictionary of Channel-
