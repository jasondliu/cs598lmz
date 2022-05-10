import codecs
codecs.register_error("strict", codecs.ignore_errors)

SUBSTITUTE_PARAM_RE = re.compile("^([a-zA-Z]+\[.*?\])$")
SUBSUBSTITUTE_PARAM_RE = re.compile("^([a-zA-Z]+)\[(.*?)\]$")

AUTHOR_RE = re.compile("^(.*?)<([^<>]+?@[^<>]+?)>$")
DATE_RE = re.compile("^([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2}):([0-9]{2})$")
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

CLEAN_RE = re.compile("\s+")
GPG_RE = re.compile("[\w]{8}([\w]{4})? [\w]{8}([
