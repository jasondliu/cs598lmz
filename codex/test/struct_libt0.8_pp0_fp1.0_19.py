import _struct

from rlp.sedes import big_endian_int

from web3.utils.encoding import (
    hexstr_if_str,
)

from web3.utils.formatters import (
    encode_hex,
)

from web3._utils.abi import (
    get_abi_input_names,
)

from web3._utils.empty import (
    empty,
)

from web3.exceptions import (
    ValidationError,
)


def make_topic_hash_hex(topic):
    """
    Converts the topic to a *topic hash* as described in the Eth docs.
    The topic hash is the first 4 bytes of the Keccak 256 hash of the topic.
    """
    if len(topic) not in {4, 32}:
        raise ValidationError(
            "Topic must be either 32 or 4 bytes, got %d bytes instead" % len(topic)
        )
    if len(topic) == 4:
        return topic
    else:
        return keccak_hex(topic)[:8]

