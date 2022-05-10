import mmap
import re

I3_ROOT = parse_config_value(file.standalone_i3)

if not I3_ROOT:
	# do not run if i3 is not in use
	exit()


I3_CONFIG_PATH = path.join(I3_ROOT, "config")

config_file = path.join(FILE_INTERNAL_PATH_CONF, "i3status.conf")

COLORS = get_colors()


def strip_i3_config(config_file = None):
	if not config_file:
		config_file = path.join(FILE_INTERNAL_PATH_CONF, "i3status.conf")

