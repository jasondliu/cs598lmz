import mmap
import os

from bing_ad_parser import BingAdParser
from log import logger


def print_results(headers, data):
    """Prints results from query."""

    output = ""
    for i, header in enumerate(headers):
        if i == 0 or (i + 1) >= len(headers):
            output += "{:<{width}}\n".format(header.upper(), width=20)
        else:
            output += "{:<{width}}\t".format(header.upper(), width=12)

    for line in data:
        for i, elem in enumerate(line):
            if i == 0 or (i + 1) >= len(headers):
                output += "{:<{width}}\n".format(elem, width=20)
            else:
                output += "{:<{width}}\t".format(elem, width=12)

    logger.debug(output)


def get_data(keyword):
    """Handles search using Bing.

    Args:
        keyword: str: Keyword to search.

