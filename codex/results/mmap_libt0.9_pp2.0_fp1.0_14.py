import mmap
import re
import os
import hashlib
import string
import random

config = configparser.ConfigParser()

parser = argparse.ArgumentParser()
parser.add_argument('config', help='path to configuration file')
args = parser.parse_args()

config.read(args.config)

messages = config['messages']
filesystem = config['filesystem']
attributes = config['attributes']
key_phrase_length = int(config['global']['key_phrase_length'])

special_tokens = colors.ENDC + colors.UNDERLINE + colors.BOLD
special_token_pattern = re.escape(special_tokens) + ".*?" + re.escape(colors.END)

def clean_banner(banner):
    banner = re.sub(special_token_pattern, "", banner)
    banner = re.sub("\n{2,}", "\n", banner)
    banner = re.sub("\n$", "", banner)
    return banner.strip()

msg_banner =
