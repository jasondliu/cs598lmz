import _struct
from .beat import Beat


class Message:
    def __init__(self, data: bytes) -> None:
        self._message = unpack(
            ">BBBBBBBBH",
            data
        )

    @property
    def magic(self) -> int:
        return self._message[0]

    @property
    def message_type(self) -> Type[Beat]:
        if self.magic > 0xA0:
            return Beat
        raise RuntimeError("Message type is unknown!")

    @property
    def message_length(self) -> int:
        return self._message[1]

    @property
    def flags(self) -> int:
        return self._message[2]

    @property
    def stream_id(self) -> int:
        return self._message[6] << 8 + self._message[7]

    @property
    def transaction_id(self) -> int:
        return _struct.unpack(">L", self._message[3:7])[0]

    @property
    def body_length(self)
