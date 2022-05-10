from lzma import LZMADecompressor
LZMADecompressor.__init__ = mock_init

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Set up test data
TEST_DATA = b"\x00\xff\xfe\xfd\xfc\xfb\xfa\xf9\xf8\xf7\xf6\xf5\xf4\xf3\xf2\xf1\xf0"
TEST_DATA_LEN = len(TEST_DATA)
TEST_DATA_CRC32 = zlib.crc32(TEST_DATA)
TEST_DATA_CHECK = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
TEST_DATA_CRC64 = zlib.crc64(TEST_DATA)
TEST_DATA_SHA256 = hashlib.sha256(TEST_DATA).digest()
TEST_DATA_SHA512 = hashlib.sha512(TEST
