from bz2 import BZ2Decompressor
BZ2Decompressor.decompress_fromfile = BZ2Decompressor.decompress_fromfile

from collections import namedtuple
from lxml import etree
import re


def parse_xml(filename, tag, namespace="", **kwargs):
    """Parse XML with lxml.etree"""

    parser = etree.XMLParser(**kwargs)
    return etree.parse(filename, parser).getroot().findall(tag, namespace)


def parse_bz2_xml(filename, tag, namespace="", **kwargs):
    """Parse bz2 compressed XML with lxml.etree"""

    with bz2.open(filename, "rb") as f:
        return parse_xml(f, tag, namespace, **kwargs)


def parse_gz_xml(filename, tag, namespace="", **kwargs):
    """Parse gzip compressed XML with lxml.etree"""

    with gzip.open(filename, "rb") as f:
        return parse_xml(f, tag, namespace, **kwargs)


def parse_text(
