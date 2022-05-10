import _struct


class Control:
    """
    Control command
    """

    # Commands
    (NOP, SET_BRIGHTNESS, SET_FADING, SET_COLOR, SAVE_COLOR, CLEAR,
     RESET_COLOR, DISABLE_DEVICE, ENABLE_DEVICE, DISABLE_LED, ENABLE_LED,
     RESET_CONTROL) = range(1, 13)

    # Status codes
    (STATUS_EXECUTING, STATUS_OK, STATUS_INVALID_ID, STATUS_INVALID_CMD,
     STATUS_INVALID_CMD_LEN, STATUS_CHECKSUM_ERROR) = range(0, 6)

    def __init__(self, protocol=None, device_id=None):
        """
        Initialize control command
        """
        # Protocol passed?
        if protocol:
            self.protocol = protocol
        else:
            self.protocol = Protocol()

        # Set device ID
        self.device_id = device_id
