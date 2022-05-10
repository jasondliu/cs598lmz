import codecs
codecs.register_error("strict", codecs.ignore_errors)

# Default user agent string
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"

# Default headers
DEFAULT_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "DNT": "1",
    "Connection": "keep-alive",
    "Cache-Control": "no-cache"
}

# Default timeout in seconds
DEFAULT_TIMEOUT = 30

# Default number of max threads
DEFAULT_MAX_THREADS = 10

# Default number of max downloads
DEFAULT_MAX_DOWNLOADS
