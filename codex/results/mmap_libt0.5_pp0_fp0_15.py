import mmap
from io import BytesIO

from oebakery import die, err, warn, info, debug
from oebakery import die, err, warn, info, debug
from oebakery import _, ngettext
from oebakery.baker import OEBakery
from oebakery.cookerutils import (CookerConfiguration,
                                  OE_CORE_DIR, OE_LAYERS_DIR,
                                  DEFAULT_CONF_FILE,
                                  DEFAULT_CONFFILES_DIR,
                                  DEFAULT_CONFFILES_MACHINE_DIR,
                                  DEFAULT_CONFFILES_DISTRO_DIR,
                                  DEFAULT_CONFFILES_DISTRO_MACHINE_DIR,
                                  DEFAULT_CONFFILES_MACHINE_DIR,
                                  DEFAULT_CONFFILES_DISTRO_DIR,
                                  DEFAULT_CONFFILES_DISTRO_MACHINE_DIR,
                                  )
from oebakery.utils import (repr_dict,
                            get_machine)
