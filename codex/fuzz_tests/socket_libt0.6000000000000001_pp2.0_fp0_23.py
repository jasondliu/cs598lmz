import socket

from . import base
from . import config
from . import utils

LOG = logging.getLogger(__name__)

CONF = cfg.CONF[__name__.split('.')[-1]]

CONFIG_SECTION = 'cloud'

CONF_GROUP = cfg.OptGroup(CONFIG_SECTION)

CONF.register_group(CONF_GROUP)

CONF.register_opts(config.OPTS)

CONF.register_opts(config.OPTS_CAPABILITIES)

CONF.register_opts(config.OPTS_IMAGE)

CONF.register_opts(config.OPTS_NETWORK)

CONF.register_opts(config.OPTS_CONTAINER)


class Cloud(base.CloudBase):

    def __init__(self):
        super(Cloud, self).__init__()

        self.config = CONF[CONFIG_SECTION]

        self.image = image.Image(self.config)

        self.network = network.Network
